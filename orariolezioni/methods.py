from orariolezioni.models import *
from operator import itemgetter

ROWS = 11
COLS = 6


def orariovuoto(titolo):
    settimana = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì']
    orari = ['08:00 - 09:00', '09:00 - 10:00', '10:00 - 11:00',
             '11:00 - 12:00', '12:00 - 13:00', '13:00 - 14:00',
             '14:00 - 15:00', '15:00 - 16:00', '16:00 - 17:00',
             '17:00 - 18:00']

    tabella = [['' for x in range(COLS)] for y in range(ROWS)]

    for i in range(1, ROWS):
        tabella[i][0] = orari[i - 1]
    for j in range(1, COLS):
        tabella[0][j] = settimana[j - 1]

    tabella[0][0] = titolo

    return tabella


def check( tab, row, column):
    if tab[row][column] == '': return True
    else: return False


def inserisci(d, c, t, o):
    # docente, corso, t = (tabella) orari delle facoltà, o = orario del docente

    ore_rimaste = c.ore_settimanali
    coordinate = []

    val = {'N.D': 0, 'LUN': 1, 'MAR': 2, 'MER': 3, 'GIO': 4, 'VEN': 5}
    lib = val[d.giorno_libero]
    imp = val[d.giorno_impegnato]
    b9 = d.prima_delle_nove
    a5 = d.dopo_le_cinque
    giorni_usati = [lib]

    # Piazza subito 2 ore nel giorno impegnato.
    if imp:
        for i in range(2, ROWS - 1, 2):
            if i != 6 and check(t,i,imp) and check(o,i,imp):
                t[i][imp] = c.nome_completo()
                t[i + 1][imp] = c.nome_completo()
                o[i][imp] = c.nome_completo()
                o[i + 1][imp] = c.nome_completo()
                giorni_usati.append(imp)
                coordinate.append([i,imp])
                coordinate.append([i+1,imp])
                ore_rimaste -= 2
                break  # Mette solo 2 ore nel giorno impegnato

    # Piazza le ore restanti, evitando il giorno libero, il giorno impegnato
    # (già controllato), le ore di pranzo e le ore marginali
    for i in range(1, COLS):
        if i not in giorni_usati and ore_rimaste > 1:
            for j in range(2, ROWS - 1, 2):
                if ore_rimaste and j != 6 and check(t,j,i) and  check(o,j,i):
                    t[j][i] = c.nome_completo()
                    t[j + 1][i] = c.nome_completo()
                    o[j][i] = c.nome_completo()
                    o[j + 1][i] = c.nome_completo()
                    giorni_usati.append(i)
                    coordinate.append([j,i])
                    coordinate.append([j+1,i])
                    ore_rimaste -= 2
                    break  # Mette solo 2 ore per giorno

    # Se rimangono delle ore, prova a creare dei blocchi da 3. Vogliamo evitare assolutamente
    # di inserire ore singole, quindi iteriamo 3 volte questi passaggi, rimuovendo
    # ogni volta un desideratum in più e ricontrollando le condizioni
    if ore_rimaste:
        del giorni_usati[0]  # Utilizza solo i giorni effettivamente impegnati
        for count in range(3):

            # Piazza la prima ora nei giorni che hanno già le prime 2 ore con quel corso
            if b9 and ore_rimaste:
                for i in giorni_usati:
                    if ore_rimaste and check(t,1,i) and t[2][i] == c.nome_completo() \
                                   and check(o,1,i) and o[2][i] == c.nome_completo():
                        t[1][i] = c.nome_completo()
                        o[1][i] = c.nome_completo()
                        coordinate.append([1,i])
                        ore_rimaste -= 1

            # Idem, ma con un blocco da 3 nelle ultime 3 ore
            if a5 and ore_rimaste:
                for i in giorni_usati:
                    if ore_rimaste and check(t,10,i) and t[9][i] == c.nome_completo()\
                                   and check(o,10,i) and o[9][i] == c.nome_completo():
                        t[10][i] = c.nome_completo()
                        o[10][i] = c.nome_completo()
                        coordinate.append([10,i])
                        ore_rimaste -= 1

            # Infine tenta di creare un blocco da 3 usando una delle ore dei pasti
            if ore_rimaste and count == 0:
                for i in giorni_usati:
                    if ore_rimaste and check(t,6,i) and t[5][i] == c.nome_completo()\
                                   and check(o,6,i) and o[5][i] == c.nome_completo():
                        t[6][i] = c.nome_completo()
                        o[6][i] = c.nome_completo()
                        coordinate.append([6,i])
                        ore_rimaste -= 1
                    elif ore_rimaste and check(t,7,i) and t[8][i] == c.nome_completo()\
                                     and check(o,7,i) and o[8][i] == c.nome_completo():
                        t[7][i] = c.nome_completo()
                        o[7][i] = c.nome_completo()
                        coordinate.append([7,i])
                        ore_rimaste -= 1

            if ore_rimaste == 0: break
            elif count == 0: b9 = True
            elif count == 1: a5 = True

    # Raramente si giungerà a questo punto con ancora ore da impegnare. E' rimasto
    # incontrollato solamente il giorno libero, quindi si proveranno a piazzare le ore
    # rimanenti in quello, prima di arrendersi e dover mettere qualche ora singola
    if ore_rimaste > 1:
        for i in range(2, ROWS - 1, 2):
            if i != 6 and check(t,i,lib) and check(o,i,lib):
                t[i][lib] = c.nome_completo()
                t[i + 1][lib] = c.nome_completo()
                o[i][lib] = c.nome_completo()
                o[i + 1][lib] = c.nome_completo()
                giorni_usati.append(lib)
                coordinate.append([i,lib])
                coordinate.append([i+1,lib])
                ore_rimaste -= 2
                break

    if ore_rimaste > 1 and lib not in giorni_usati:
        if check(t,6,lib) and check(o,6,lib) and check(t,7,lib) and check(o,7,lib):
            t[6][lib] = c.nome_completo()
            o[6][lib] = c.nome_completo()
            t[7][lib] = c.nome_completo()
            o[7][lib] = c.nome_completo()
            coordinate.append([6,lib])
            coordinate.append([7,lib])
            ore_rimaste -= 2

    # Dichiarazione di resa. Se a questo punto ci sono ancora ore da inserire,
    # vengono piazzate dove c'è spazio, creando purtroppo un brutto orario finale.
    if ore_rimaste:
        for i in range(1, COLS):
            for j in range(1, ROWS):
                if ore_rimaste and check(t,j,i) and check(o,j,i):
                    t[j][i] = c.nome_completo()
                    o[j][i] = c.nome_completo()
                    coordinate.append([j,i])
                    ore_rimaste -= 1

    return (t, o, coordinate)


def aggiungi_a(tab, coord, *args):

    # Riempie la tabella tab con gli oggetti args, seguendo le coordinate passate
    # in ingresso. Il caso di 3 args è dedicato all'inserimento delle aule, ma la
    # funzione può comunque essere utilizzata per scopi generici, con un solo arg
    # passato in ingresso.
    for i in coord:
        tab[i[0]][i[1]] = args[0]

    if args.__len__() == 3: # Caso inserimento aule -> args contiene aula, lab e ore_lab
        map_per_giorno = set(map(itemgetter(1), coord))
        gruppi_per_giorno = [[[i[0],i[1]] for i in coord if i[1]==j] for j in map_per_giorno]
        ore_lab = args[2]
        for i in gruppi_per_giorno:
            if args[2] == gruppi_per_giorno.__len__():
                tab[i[0][0]][i[0][1]] = args[1] # dedica la prima ora di ogni giorno al lab
                ore_lab -= 1
            elif args[2] == i.__len__():
                for j in i:
                    tab[j[0]][j[1]] = args[1] # dedica un giorno intero al laboratorio
                    ore_lab -= 1
                break
        if ore_lab: # se le ore di lab sono irregolari, riempie giorni finchè non le esaurisce
            for i in range(ore_lab):
                tab[coord[i][0]][coord[i][1]] = args[1]
    return tab





def assegna_aula(c, aule_usate):

    aule = aula.objects.filter(facolta__id=c.facolta_id).order_by('capienza')

    for i in aule:
        if not i.laboratorio and i not in aule_usate and c.numero_studenti <= i.capienza:
            aule_usate.append(i)
            return i.codice

    for i in aule:
        if not i.laboratorio and c.numero_studenti <= i.capienza:
            return i.codice

    for i in aule:
        if c.numero_studenti <= i.capienza:
            return i.codice

    # Punto mai raggiunto, date le condizioni di validazione del modello Aula
    return

def assegna_laboratorio(c, aule_usate):

    lab = aula.objects.filter(facolta__id=c.facolta_id, laboratorio=True).order_by('capienza')

    for i in lab:
        if i not in aule_usate and c.numero_studenti <= i.capienza:
            aule_usate.append(i)
            return i.codice

    for i in lab:
        if c.numero_studenti <= i.capienza:
            return i.codice

    # Punto mai raggiunto, date le condizioni di validazione del modello Aula
    return


def crea_orari():
    
    # QuerySet che ordina tutti i docenti in base al valore di fitness di ciascuno.
    docenti_ordinati = sorted(docente.objects.all(),
                              key=lambda d: d.__fitness__(),
                              reverse=True)
    
    # Per ogni facoltà crea due tabelle di orari, inizialmente vuote. Una per l'orario
    # dei corsi e una identica per i rispettivi orari delle aule.
    orari_corsi, orari_aule = [], []
    for i in facolta.objects.all():
        orari_corsi.append(orariovuoto(i.nome))
        orari_aule.append(orariovuoto(i.nome))
        
    # Per ogni docente (in ordine) crea una tabella che conterrà il suo orario personale.
    orari_docenti = []
    for i in docenti_ordinati:
        titolo = i.nome + " " + i.cognome
        orari_docenti.append(orariovuoto(titolo))

    # Tiene conto delle aule già impegnate per i corsi. Serve per garantire una copertura
    # il più completa possibile delle stanze a disposizione.
    aule_assegnate = []

    # A partire dai docenti più "meritevoli" si inseriscono i corsi nell'orario
    for index, doc in enumerate(docenti_ordinati):
        for crs in doc.corso_set.all():
                # results[0] = orario di facoltà, aggiornato col nuovo corso
                # results[1] = orario del docente, aggiornato col nuovo corso
                # results[2] = giorni e ore occupate. Serve per assegnare le aule al corso
                results = inserisci(doc,
                                    crs,
                                    orari_corsi[crs.facolta_id - 1],
                                    orari_docenti[index])
                orari_corsi[crs.facolta_id - 1] = results[0]
                orari_docenti[index] = results[1]

                lab = ''
                if crs.ore_laboratorio:
                    lab = assegna_laboratorio(crs, aule_assegnate)
                room = assegna_aula(crs, aule_assegnate)

                orari_aule[crs.facolta_id - 1] = aggiungi_a(orari_aule[crs.facolta_id - 1],
                                                          results[2], room, lab,
                                                          crs.ore_laboratorio)


    return (orari_corsi, orari_docenti, orari_aule)
