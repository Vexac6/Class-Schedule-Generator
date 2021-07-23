from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from .methods import *
from random import randint


class OrariTest(TestCase):

    @classmethod
    def setUpClass(cls):

        super(OrariTest, cls).setUpClass()

        f01 = facolta.objects.create(nome='Medicina', codice='MED-01')
        f02 = facolta.objects.create(nome='Economia', codice='ECO-01')
        f03 = facolta.objects.create(nome='Matematica', codice='MAT-01')
        f04 = facolta.objects.create(nome='Informatica', codice='MAT-03')
        f05 = facolta.objects.create(nome='Ingegneria Genetica', codice='ING-07')
        f06 = facolta.objects.create(nome='Ingegneria Informatica', codice='ING-04')
        d01 = docente.objects.create(nome='Stefania',
                                     cognome='Statis',
                                     email='stefaniastatis@universita.com',
                                     registration_key='OWUE5',
                                     giorno_libero='MER',
                                     giorno_impegnato='N.D',
                                     prima_delle_nove=False,
                                     dopo_le_cinque=False)
        d02 = docente.objects.create(nome='Stefano',
                                     cognome='Stati',
                                     email='stefanostati@universita.com',
                                     registration_key='9UEBR',
                                     giorno_libero='N.D',
                                     giorno_impegnato='N.D',
                                     prima_delle_nove=False,
                                     dopo_le_cinque=True)
        d03 = docente.objects.create(nome='Antonio',
                                     cognome='Antani',
                                     email='antonioantani@universita.com',
                                     registration_key='P5WE9',
                                     giorno_libero='LUN',
                                     giorno_impegnato='MAR',
                                     prima_delle_nove=True,
                                     dopo_le_cinque=False)
        d04 = docente.objects.create(nome='Fabrizio',
                                     cognome='Farmaci',
                                     email='fabriziofarmaci@universita.com',
                                     registration_key='N0782',
                                     giorno_libero='LUN',
                                     giorno_impegnato='GIO',
                                     prima_delle_nove=False,
                                     dopo_le_cinque=True)
        d05 = docente.objects.create(nome='John',
                                     cognome='Doe',
                                     email='johndoe@universita.com',
                                     registration_key='097S8',
                                     giorno_libero='LUN',
                                     giorno_impegnato='MAR',
                                     prima_delle_nove=True,
                                     dopo_le_cinque=True)
        d06 = docente.objects.create(nome='Ignazio',
                                     cognome='Informa',
                                     email='ignazioinforma@universita.com',
                                     registration_key='08BC3',
                                     giorno_libero='MER',
                                     giorno_impegnato='GIO',
                                     prima_delle_nove=True,
                                     dopo_le_cinque=False)
        d07 = docente.objects.create(nome='Anna',
                                     cognome='Lisi',
                                     email='annalisi@universita.com',
                                     registration_key='2I38B',
                                     giorno_libero='N.D',
                                     giorno_impegnato='N.D',
                                     prima_delle_nove=True,
                                     dopo_le_cinque=True)
        d08 = docente.objects.create(nome='Matteo',
                                     cognome='Matico',
                                     email='matteomatico@universita.com',
                                     registration_key='C3N9N',
                                     giorno_libero='GIO',
                                     giorno_impegnato='LUN',
                                     prima_delle_nove=False,
                                     dopo_le_cinque=True)
        d09 = docente.objects.create(nome='Aldo',
                                     cognome='Gebra',
                                     email='aldogebra@universita.com',
                                     registration_key='NDCWW',
                                     giorno_libero='VEN',
                                     giorno_impegnato='GIO',
                                     prima_delle_nove=False,
                                     dopo_le_cinque=False)
        d10 = docente.objects.create(nome='Pippo',
                                     cognome='Programmi',
                                     email='pippoprogrammi@universita.com',
                                     registration_key='MQD3I',
                                     giorno_libero='VEN',
                                     giorno_impegnato='GIO',
                                     prima_delle_nove=False,
                                     dopo_le_cinque=False)
        d11 = docente.objects.create(nome='Sisto',
                                     cognome='Temi',
                                     email='sistotemi@universita.com',
                                     registration_key='MAHD2',
                                     giorno_libero='VEN',
                                     giorno_impegnato='LUN',
                                     prima_delle_nove=True,
                                     dopo_le_cinque=False)
        d12 = docente.objects.create(nome='Margaret',
                                     cognome='Thatcher',
                                     email='margaretthatcher@universita.com',
                                     registration_key='X923U',
                                     giorno_libero='N.D',
                                     giorno_impegnato='N.D',
                                     prima_delle_nove=False,
                                     dopo_le_cinque=False)
        aula.objects.create(codice='MED01',
                            facolta=f01,
                            capienza=100,
                            laboratorio=False)
        aula.objects.create(codice='MED03',
                            facolta=f01,
                            capienza=50,
                            laboratorio=False)
        aula.objects.create(codice='MED04',
                            facolta=f01,
                            capienza=40,
                            laboratorio=False)
        aula.objects.create(codice='MED12',
                            facolta=f01,
                            capienza=60,
                            laboratorio=True)
        aula.objects.create(codice='MED13',
                            facolta=f01,
                            capienza=45,
                            laboratorio=True)
        aula.objects.create(codice='ECO-1',
                            facolta=f02,
                            capienza=80,
                            laboratorio=False)
        aula.objects.create(codice='ECO-2',
                            facolta=f02,
                            capienza=60,
                            laboratorio=False)
        aula.objects.create(codice='ECO-3',
                            facolta=f02,
                            capienza=40,
                            laboratorio=False)
        aula.objects.create(codice='ECO-L',
                            facolta=f02,
                            capienza=50,
                            laboratorio=True)
        aula.objects.create(codice='M-1/A',
                            facolta=f03,
                            capienza=100,
                            laboratorio=False)
        aula.objects.create(codice='M-1/B',
                            facolta=f03,
                            capienza=80,
                            laboratorio=False)
        aula.objects.create(codice='M-1/D',
                            facolta=f03,
                            capienza=25,
                            laboratorio=False)
        aula.objects.create(codice='M-2/F',
                            facolta=f03,
                            capienza=40,
                            laboratorio=True)
        aula.objects.create(codice='M-1/C',
                            facolta=f04,
                            capienza=60,
                            laboratorio=False)
        aula.objects.create(codice='M-1/E',
                            facolta=f04,
                            capienza=30,
                            laboratorio=False)
        aula.objects.create(codice='M-2/A',
                            facolta=f04,
                            capienza=50,
                            laboratorio=True)
        aula.objects.create(codice='M-2/B',
                            facolta=f04,
                            capienza=40,
                            laboratorio=True)
        aula.objects.create(codice='M-2/C',
                            facolta=f04,
                            capienza=30,
                            laboratorio=True)
        aula.objects.create(codice='ING01',
                            facolta=f05,
                            capienza=100,
                            laboratorio=False)
        aula.objects.create(codice='ING04',
                            facolta=f05,
                            capienza=50,
                            laboratorio=False)
        aula.objects.create(codice='ING05',
                            facolta=f05,
                            capienza=35,
                            laboratorio=True)
        aula.objects.create(codice='ING06',
                            facolta=f05,
                            capienza=40,
                            laboratorio=True)
        aula.objects.create(codice='ING02',
                            facolta=f06,
                            capienza=90,
                            laboratorio=False)
        aula.objects.create(codice='ING12',
                            facolta=f06,
                            capienza=60,
                            laboratorio=True)
        aula.objects.create(codice='ING13',
                            facolta=f06,
                            capienza=50,
                            laboratorio=True)
        aula.objects.create(codice='ING15',
                            facolta=f06,
                            capienza=30,
                            laboratorio=True)
        corso.objects.create(nome='Statistica',
                             docenti=d01,
                             facolta=f01,
                             crediti=2,
                             ore_settimanali=2,
                             ore_laboratorio=0,
                             numero_studenti=30)
        corso.objects.create(nome='Anatomia',
                             docenti=d03,
                             facolta=f01,
                             crediti=12,
                             ore_settimanali=10,
                             ore_laboratorio=4,
                             numero_studenti=60)
        corso.objects.create(nome='Farmacologia',
                             docenti=d04,
                             facolta=f01,
                             crediti=10,
                             ore_settimanali=8,
                             ore_laboratorio=6,
                             numero_studenti=30)
        corso.objects.create(nome='Inglese Tecnico',
                             docenti=d05,
                             facolta=f01,
                             crediti=3,
                             ore_settimanali=2,
                             ore_laboratorio=0,
                             numero_studenti=80)
        corso.objects.create(nome='Statistica',
                             docenti=d01,
                             facolta=f02,
                             crediti=10,
                             ore_settimanali=8,
                             ore_laboratorio=0,
                             numero_studenti=40)
        corso.objects.create(nome='Informatica',
                             docenti=d06,
                             facolta=f02,
                             crediti=6,
                             ore_settimanali=4,
                             ore_laboratorio=4,
                             numero_studenti=25)
        corso.objects.create(nome='Analisi Matematica',
                             docenti=d07,
                             facolta=f02,
                             crediti=10,
                             ore_settimanali=8,
                             ore_laboratorio=0,
                             numero_studenti=30)
        corso.objects.create(nome='Analisi Matematica',
                             docenti=d07,
                             facolta=f03,
                             crediti=15,
                             ore_settimanali=10,
                             ore_laboratorio=0,
                             numero_studenti=60)
        corso.objects.create(nome='Algebra Lineare',
                             docenti=d09,
                             facolta=f03,
                             crediti=9,
                             ore_settimanali=6,
                             ore_laboratorio=0,
                             numero_studenti=50)
        corso.objects.create(nome='Informatica',
                             docenti=d06,
                             facolta=f03,
                             crediti=6,
                             ore_settimanali=4,
                             ore_laboratorio=4,
                             numero_studenti=40)
        corso.objects.create(nome='Programmazione',
                             docenti=d10,
                             facolta=f04,
                             crediti=9,
                             ore_settimanali=6,
                             ore_laboratorio=6,
                             numero_studenti=40)
        corso.objects.create(nome='Sistemi Operativi',
                             docenti=d11,
                             facolta=f04,
                             crediti=9,
                             ore_settimanali=6,
                             ore_laboratorio=2,
                             numero_studenti=30)
        corso.objects.create(nome='Algebra Lineare',
                             docenti=d09,
                             facolta=f04,
                             crediti=9,
                             ore_settimanali=6,
                             ore_laboratorio=0,
                             numero_studenti=30)
        corso.objects.create(nome='Biologia',
                             docenti=d03,
                             facolta=f05,
                             crediti=6,
                             ore_settimanali=4,
                             ore_laboratorio=0,
                             numero_studenti=35)
        corso.objects.create(nome='Analisi Matematica',
                             docenti=d03,
                             facolta=f05,
                             crediti=9,
                             ore_settimanali=6,
                             ore_laboratorio=0,
                             numero_studenti=50)
        corso.objects.create(nome='Statistica',
                             docenti=d02,
                             facolta=f05,
                             crediti=9,
                             ore_settimanali=8,
                             ore_laboratorio=4,
                             numero_studenti=40)
        corso.objects.create(nome='Inglese Tecnico',
                             docenti=d05,
                             facolta=f05,
                             crediti=3,
                             ore_settimanali=4,
                             ore_laboratorio=0,
                             numero_studenti=50)
        corso.objects.create(nome='Sistemi Operativi',
                             docenti=d11,
                             facolta=f06,
                             crediti=9,
                             ore_settimanali=8,
                             ore_laboratorio=6,
                             numero_studenti=40)
        corso.objects.create(nome='Inglese',
                             docenti=d12,
                             facolta=f06,
                             crediti=3,
                             ore_settimanali=2,
                             ore_laboratorio=0,
                             numero_studenti=60)
        corso.objects.create(nome='Programmazione a Oggetti',
                             docenti=d06,
                             facolta=f06,
                             crediti=9,
                             ore_settimanali=6,
                             ore_laboratorio=6,
                             numero_studenti=50)
        corso.objects.create(nome='Matematica del Continuo',
                             docenti=d08,
                             facolta=f06,
                             crediti=9,
                             ore_settimanali=6,
                             ore_laboratorio=0,
                             numero_studenti=60)


    def pretty_print(self, matrix):
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))


    def get_docente(self, nome_completo):
        for doc in docente.objects.all():
            nc = doc.nome + ' ' + doc.cognome
            if nc == nome_completo:
                return docente.objects.get(id=doc.id)


    def get_corso(self, nome_completo):
        for crs in corso.objects.all():
            if crs.nome_completo() == nome_completo:
                return corso.objects.get(id=crs.id)


    def test_corso_troppe_ore(self):
        # ------------------------------------------------------------------------
        # Controlla non si possa creare un corso con troppe ore di lezione, che
        # quindi uscirebbe dall'orario settimanale, se sommato agli altri.
        # ------------------------------------------------------------------------
        fac = facolta.objects.get(id=1) # Medicina ha 22 ore occupate, quindi 28 disponibili
        doc = docente.objects.get(id=1) # Serve solo per l'integrità referenziale

        crs = corso.objects.create(nome='Test',
                            facolta=fac,
                            docenti=doc,
                            ore_settimanali=29) # Per N>28, il test è sempre valido

        with self.assertRaises(ValidationError):
            crs.clean()

        crs.ore_settimanali = 28
        try:
            crs.clean()
        except:
            self.fail('Qualcosa è andato storto! Il corso avrebbe dovuto essere creato con successo!')

        crs.delete()


    def test_corso_troppi_studenti_1(self):
        # ------------------------------------------------------------------------
        # Controlla non si possa creare un corso con troppi studenti, che non
        # sarebbe possibile assegnare a nessun aula di quella facoltà.
        # ------------------------------------------------------------------------
        fac = facolta.objects.get(id=4) # L'aula più grande di Informatica ha 60 posti
        doc = docente.objects.get(id=1)

        crs = corso.objects.create(nome='Test',
                            facolta=fac,
                            docenti=doc,
                            numero_studenti=61) # Per N>60, il test è sempre valido

        with self.assertRaises(ValidationError):
            crs.clean()

        crs.numero_studenti = 60
        try:
            crs.clean()
        except:
            self.fail('Qualcosa è andato storto! Il corso avrebbe dovuto essere creato con successo!')

        crs.delete()


    def test_corso_troppi_studenti_2(self):
        # ------------------------------------------------------------------------
        # Controlla non si possa creare un corso con troppi studenti, che non
        # sarebbe possibile assegnare a nessun laboratorio di quella facoltà.
        # ------------------------------------------------------------------------
        fac = facolta.objects.get(id=4) # Il laboratorio più grande di Informatica ha 50 posti
        doc = docente.objects.get(id=1)

        crs = corso.objects.create(nome='Test',
                            facolta=fac,
                            docenti=doc,
                            ore_settimanali=2,
                            ore_laboratorio=1,
                            numero_studenti=51) # Per N>50, il test è sempre valido

        with self.assertRaises(ValidationError):
            crs.clean()

        crs.numero_studenti = 50
        try:
            crs.clean()
        except:
            self.fail('Qualcosa è andato storto! Il corso avrebbe dovuto essere creato con successo!')

        crs.delete()

    def test_calcolatore_completezza_corsi(self):
        # ------------------------------------------------------------------------
        # Il calcolatore deve sempre scrivere ogni corso, anche senza rispettare i
        # desiderata, se le condizioni richieste sono avverse
        # ------------------------------------------------------------------------
        # HOW TO USE: Modifica parti del test per produrre risultati diversi.
        # LEGENDA:
        #          "+" significa che un valore può essere modificato
        #          "x" significa che la riga può essere commentata (#)
        # ------------------------------------------------------------------------
        giorni = {0: 'N.D', 1: 'LUN', 2: 'MAR', 3: 'MER', 4: 'GIO', 5: 'VEN'}
        cycles = 20  # + N°iterazioni dei test. Sii buono col processore.

        for iterazioni in range(cycles):
            if cycles > 1: # Con una sola iterazione del test usa i dati originali
                for c in corso.objects.all():
                    c.ore_settimanali = randint(2, 8)                     # x+
                    c.ore_laboratorio = randint(0, c.ore_settimanali)     # x
                    c.crediti = randint                                   # x
                    # c.ore_settimanali = 6                                # x+
                    # c.ore_laboratorio = 2                                # x+
                    # c.crediti = 6                                        # x+

                for i in docente.objects.all():
                    i.giorno_libero = giorni[randint(0, 5)]               # x
                    i.giorno_impegnato = giorni[randint(0, 5)]            # x
                    i.prima_delle_nove = bool(randint(0, 1))              # x
                    i.dopo_le_cinque = bool(randint(0, 1))                # x
                    # i.giorno_libero = 'LUN'                              # x+
                    # i.giorno_impegnato = 'MAR'                           # x+
                    # i.prima_delle_nove = True                            # x+
                    # i.dopo_le_cinque = False                             # x+

            tab = crea_orari()[0]
            #for i in tab:             # x  Scommentare per stampare l'orario delle
                #self.pretty_print(i)  # x  lezioni. Magari con poche iterazioni.

            array = []
            for i in tab:
                for j in i:
                    for k in j:
                        array.append(k)

            for crs in corso.objects.all():
                self.assertIn(crs.nome_completo(), array)


    def test_calcolatore_non_sovrapposizione_docenti(self):
        # ------------------------------------------------------------------------
        # Il calcolatore deve scrivere l'orario di ogni docente senza sovrapporre
        # due corsi diversi alla stessa ora. E' testato controllando che ad ogni
        # ora di lezione di quel docente non ci siano altri corsi tenuti dallo stesso
        # in tutte le altre facoltà.
        # ------------------------------------------------------------------------
        # Questo test è decisamente pesante, quindi verrà iterato una volta sola.
        # ------------------------------------------------------------------------
        # HOW TO USE: Modifica parti del test per produrre risultati diversi.
        # LEGENDA:
        #          "+" significa che un valore può essere modificato
        #          "x" significa che la riga può essere commentata (#)
        # ------------------------------------------------------------------------
        giorni = {0: 'N.D', 1: 'LUN', 2: 'MAR', 3: 'MER', 4: 'GIO', 5: 'VEN'}
        for c in corso.objects.all():
            c.ore_settimanali = randint(2, 8)                      # x+
            c.ore_laboratorio = randint(0, c.ore_settimanali)      # x
            c.crediti = randint                                    # x
            # c.ore_settimanali = 6                                 # x+
            # c.ore_laboratorio = 2                                 # x+
            # c.crediti = 6                                         # x+

        for i in docente.objects.all():
            i.giorno_libero = giorni[randint(0, 5)]                # x
            i.giorno_impegnato = giorni[randint(0, 5)]             # x
            i.prima_delle_nove = bool(randint(0, 1))               # x
            i.dopo_le_cinque = bool(randint(0, 1))                 # x
            # i.giorno_libero = 'LUN'                               # x+
            # i.giorno_impegnato = 'MAR'                            # x+
            # i.prima_delle_nove = True                             # x+
            # i.dopo_le_cinque = False                              # x+

        for i in corso.objects.all():
            id = randint(1, docente.objects.all().__len__() + 1)
            for j in docente.objects.all():
                if j.id == id:
                    i.docenti = j
                    i.save()

        results = crea_orari()
        orari_crs = results[0]
        orari_doc = results[1]
        # for i in orari_doc:        # x   Scommentare per stampare gli orari dei
            # self.pretty_print(i)   # x   docenti. Magari con poche iterazioni.

        for i in orari_doc:
            doc = self.get_docente(i[0][0])
            for index, j in enumerate(i):
                for idx, k in enumerate(j):
                    if index > 0 and idx > 0 and k != '':
                        for fac in orari_crs:
                            if fac[index][idx] != '' and fac[index][idx] != k:
                                crs = self.get_corso(fac[index][idx])
                                self.assertNotIn(crs, doc.corso_set.all())


    def test_view_index_utente_registrato(self):
        # ------------------------------------------------------------------------
        # Controlla che un utente registrato al sito possa accedere alle
        # funzionalità dedicate ai docenti (tipo vedere l'orario personale)
        # ------------------------------------------------------------------------
        random_docente = randint(1, docente.objects.all().__len__())
        email = ''
        for doc in docente.objects.all():
            if doc.id == random_docente:
                email = doc.email

        user = User.objects.create_user(username='Testolino',
                                        email=email,
                                        password='testtest')
        self.client.login(username='Testolino', password='testtest')
        response = self.client.get(reverse('orariolezioni:index'))
        self.assertContains(response, 'Orario personale')
        self.assertContains(response, 'Logout')
        self.assertContains(response, user.username)


    def test_view_index_utente_qualsiasi(self):
        # ------------------------------------------------------------------------
        # Controlla l'opposto della view precedente
        # ------------------------------------------------------------------------
        response = self.client.get(reverse('orariolezioni:index'))
        self.assertNotContains(response, 'Orario personale')
        self.assertNotContains(response, 'Logout')


    def test_view_orario_docente_utente_qualsiasi(self):
        # ------------------------------------------------------------------------
        # Controlla che un utente non registrato non possa accedere forzatamente
        # all'orario delle lezioni di un docente, inserendone l'URL. Per farlo,
        # viene controllata la diretta conseguenza del fatto, ovvero la
        # redirezione alla pagina di login.
        # ------------------------------------------------------------------------
        response = self.client.get(reverse('orariolezioni:orario_d'), follow=True)
        self.assertContains(response, 'Pagina di login')


    def test_view_orario_docente_utente_registrato_ma_non_come_docente(self):
        # ------------------------------------------------------------------------
        # L'Admin (oltre ad esserne lui stesso un caso) ha la facoltà di creare
        # utenti senza associarli a nessun docente. Questo consente ad essi di
        # accedere alla pagina dell'orario personale, ma si vuole che possano
        # soltanto vedere un errore 404:NotFound.
        # ------------------------------------------------------------------------
        User.objects.create_user(username='UserSenzaEmail',
                                 password='sonosenzaemail')
        User.objects.create_user(username='UserConEmailSbagliata',
                                 password='hosbagliatoemail',
                                 email='questanonvabene@gmail.com')

        self.client.login(username='UserSenzaEmail', password='sonosenzaemail')
        response = self.client.get(reverse('orariolezioni:orario_d'), follow=True)
        self.assertEqual(response.status_code, 404)

        self.client.login(username='UserConEmailSbagliata', password='hosbagliatoemail')
        response = self.client.get(reverse('orariolezioni:orario_d'), follow=True)
        self.assertEqual(response.status_code, 404)


    def test_view_orario_lezioni_bel_nome(self):
        # ------------------------------------------------------------------------
        # Controlla che un utente registrato al sito possa accedere alle
        # funzionalità dedicate ai docenti (tipo vedere l'orario personale)
        # ------------------------------------------------------------------------
        random_docente = randint(1, docente.objects.all().__len__())
        email = ''
        for doc in docente.objects.all():
            if doc.id == random_docente:
                email = doc.email

        user = User.objects.create_user(username='Testolino',
                                        email=email,
                                        password='testtest')
        self.client.login(username='Testolino', password='testtest')
        response = self.client.get(reverse('orariolezioni:index'))
        self.assertContains(response, 'Orario personale')
        self.assertContains(response, 'Logout')
        self.assertContains(response, user.username)