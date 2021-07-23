from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from orariolezioni.models import docente

class Command(BaseCommand):
    help = 'Crea un utente inserendo la chiave di registrazione presente nel ' \
           'database relativa a un docente. Verrà creato un nuovo utente con ' \
           'username=nome+cognome del docente e password "nuovoutente", mentre ' \
           'gli altri dati rimarranno fedeli a quelli del docente nel database.'

    def add_arguments(self, parser):
        parser.add_argument('reg_key', nargs=1, type=str)

    def handle(self, *args, **options):
        try:
            doc = docente.objects.get(registration_key=options['reg_key'][0])
        except docente.DoesNotExist:
            raise CommandError('La chiave inserita non corrisponde a nessun docente!\n')
        user = User.objects.create_user(username=doc.nome + doc.cognome,
                                        email=doc.email,
                                        password='nuovoutente')
        user.first_name = doc.nome
        user.last_name = doc.cognome
        user.save()
        self.stdout.write(self.style.SUCCESS('Utente "%s" creato con successo!' % user.username))
