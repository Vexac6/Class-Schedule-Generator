from django.contrib import admin
from .models import aula, corso, facolta, docente

# Register your models here.


class CorsoAdmin (admin.ModelAdmin):

    list_filter = ['docenti', 'facolta']
    list_display = ['__str__', 'crediti', 'ore_settimanali', 'ore_laboratorio', 'numero_studenti']
    fieldsets = [
        (None,  {'fields': ['nome']}),
        (None,  {'fields': ['docenti']}),
        (None,  {'fields': ['facolta']}),
        ('Dettagli del Corso', {'fields': ['crediti',
                                           'ore_settimanali',
                                           'ore_laboratorio',
                                           'numero_studenti',]}),
    ]


class AulaAdmin (admin.ModelAdmin):

    list_filter = ['facolta', 'laboratorio']
    list_display = ['__str__', 'facolta', 'capienza', 'laboratorio']


class DocenteAdmin (admin.ModelAdmin):

    list_display = ['__str__', 'giorno_libero', 'giorno_impegnato',
                    'prima_delle_nove', 'dopo_le_cinque']

    fieldsets = [
        (None, {'fields': ['nome']}),
        (None, {'fields': ['cognome']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['registration_key']}),
        ('Desiderata', {'fields': ['giorno_libero',
                                   'giorno_impegnato',
                                   'prima_delle_nove',
                                   'dopo_le_cinque']}),
    ]


admin.site.register(corso, CorsoAdmin)
admin.site.register(docente, DocenteAdmin)
admin.site.register(facolta)
admin.site.register(aula, AulaAdmin)
