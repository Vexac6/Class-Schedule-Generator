from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .methods import *


def index(request):
    lista_fac = facolta.objects.order_by('id')
    context = {'lista_fac': lista_fac}
    return render(request, "orariolezioni/index.html", context)


def orario_facolta(request, facolta_id):
    fac = get_object_or_404(facolta, id=facolta_id)

    results = crea_orari()
    orari, aule = results[0], results[2]
    tab, tab2 = [], []
    for i in range(orari.__len__()):
        if orari[i][0][0] == fac.nome:
            tab = orari[i]
        if aule[i][0][0] == fac.nome:
            tab2 = aule[i]
    crs = tab
    for index,i in enumerate(tab):
        for idx, j in enumerate(i):
            if index>0 and idx>0 and j!='':
                crs[index][idx] = tab[index][idx][:-9]

    context = {'nome': fac.nome, 'tabella': crs, 'aule': tab2}

    return render(request, "orariolezioni/orario.html", context)


@login_required
def orario_docente(request):
    doc = get_object_or_404(docente, email=request.user.email)

    results = crea_orari()
    corsi, personale, aule = results[0], results[1], results[2]
    tab = []
    tab2 = orariovuoto(doc.nome + " " + doc.cognome)
    for i in range(personale.__len__()):
        if personale[i][0][0] == (doc.nome + " " + doc.cognome):
            tab = personale[i]
    for i in range(tab.__len__()):
        for j in range(tab[i].__len__()):
            if tab[i][j] != '':
                for k in range(corsi.__len__()):
                    if corsi[k][i][j] == tab[i][j]:
                        tab2[i][j] = aule[k][i][j]

    context = {'nome': doc.nome + " " + doc.cognome, 'tabella': tab, 'aule': tab2}
    return render(request, "orariolezioni/orario.html", context)
