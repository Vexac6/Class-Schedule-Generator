from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.
# Le classi in minuscolo servono a postgresql per mantenere l'integrità delle relazioni

SETTIMANA = (
        ('N.D', 'Indifferente'),
        ('LUN', 'Lunedì'),
        ('MAR', 'Martedì'),
        ('MER', 'Mercoledì'),
        ('GIO', 'Giovedì'),
        ('VEN', 'Venerdì'),
    )

class docente(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, unique=True)
    registration_key = models.CharField(max_length=5, default='', unique=True)

    giorno_libero = models.CharField(max_length=3, choices=SETTIMANA, default='N.D')
    giorno_impegnato = models.CharField(max_length=3, choices=SETTIMANA, default='N.D')
    prima_delle_nove = models.BooleanField(default=False)
    dopo_le_cinque = models.BooleanField(default=False)

    def __fitness__(self):
        fitness = self.corso_set.count() * 11
        if self.prima_delle_nove: fitness += 1
        if self.dopo_le_cinque: fitness += 1
        if self.giorno_impegnato != 'N.D': fitness += 1
        if self.giorno_libero == 'N.D': fitness += 2
        else: fitness -= 1

        return fitness

    def clean(self):
        if self.giorno_libero == self.giorno_impegnato and self.giorno_libero != 'N.D':
            raise ValidationError(_("Il giorno libero e quello impegnato coincidono!"))
        if self.registration_key.__len__() != 5:
            raise ValidationError(_("Devi inserire una Registration Key di 5 caratteri!"))

    def __str__(self):
        nome_completo = self.nome + " " + self.cognome
        return nome_completo

    class Meta:
        verbose_name_plural = 'docenti'
        unique_together = ('nome', 'cognome')


class facolta(models.Model):
    nome = models.CharField(max_length=30)
    codice = models.CharField(max_length=6,
                              default='AAA-00',
                              validators=[RegexValidator(regex='[A-Z][A-Z][A-Z]-[\d][\d]',
                                                         message='Inserisci un codice del '
                                                                 'tipo "AAA-00"',

                              ),],
                              unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'facoltà'


class corso(models.Model):
    nome = models.CharField(max_length=50, default='')

    docenti = models.ForeignKey(docente)
    facolta = models.ForeignKey(facolta, on_delete=models.CASCADE, null=True)

    crediti = models.PositiveSmallIntegerField(default=0)
    ore_settimanali = models.PositiveSmallIntegerField(default=0)
    ore_laboratorio = models.PositiveSmallIntegerField(default=0)
    numero_studenti = models.PositiveIntegerField(default=0)

    def nome_completo(self):
        return self.nome + ' / ' + self.facolta.codice

    def __str__(self):
        return self.nome_completo()

    def clean(self):
        if self.ore_laboratorio > self.ore_settimanali:
            raise ValidationError(_('Ci sono più ore di laboratorio che ore totali!'))
        ore_tot = corso.objects.filter(facolta=self.facolta)\
                               .exclude(id=self.id)\
                               .aggregate(Sum('ore_settimanali'))
        if ore_tot['ore_settimanali__sum'] != None:
            if ore_tot['ore_settimanali__sum'] + self.ore_settimanali > 50:
                raise ValidationError(_('Questo corso ha troppe ore e non può essere inserito'
                                        ' nell\'orario settimanale!'))
        aule_fac = aula.objects\
            .filter(facolta_id=self.facolta_id).order_by('-capienza')
        lab_fac = aula.objects\
            .filter(facolta_id=self.facolta_id, laboratorio=True).order_by('-capienza')
        if self.numero_studenti > aule_fac[0].capienza:
            raise ValidationError(_('Al momento non c\'è un aula in grado di contenere tutti'
                                    ' questi studenti! Diminuisci il numero di studenti o '
                                    'crea una nuova aula che possa contenerli!'))
        if self.ore_laboratorio and self.numero_studenti > lab_fac[0].capienza:
            raise ValidationError(_('Al momento non c\'è un laboratorio in grado di contenere '
                                    'tutti questi studenti! Diminuisci il numero di studenti '
                                    'o crea un nuovo laboratorio che possa contenerli!'))


    class Meta:
        verbose_name_plural = 'corsi'
        unique_together = ('nome','facolta')


class aula(models.Model):
    codice = models.CharField(max_length=5, primary_key=True)
    facolta = models.ForeignKey(facolta, on_delete=models.CASCADE, null=True)
    capienza = models.PositiveIntegerField(default=25)
    laboratorio = models.BooleanField(default=False)

    def __str__(self):
        return self.codice

    def clean(self):
        if self.capienza < 25:
            raise ValidationError(_('Un aula deve avere almeno 25 posti.'))

    class Meta:
        verbose_name_plural = 'aule'
