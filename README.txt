*******************************************************************************
* ORARIOLEZIONI
* Creator: Nicolò Cavedoni - 66573 - Informatica-UniMoRe
* 
* HOW TO USE
*******************************************************************************
* 0) PREREQUISITI:
*	a) Aver installato un interprete Python e il tool Pip
*	b) Aver installato Django (disponibile attraverso pip install Django) 
*	c) Aver installato PostgreSQL
*
* 1) CREAZIONE DATABASE POSTGRES
*    Da linea di comando:
*	a) Autenticarsi su postgres -> $ sudo su postgres
*	b) Avviare il terminale di postgres -> $ psql
*       c) Ripetere esattamente questi passaggi:
*	d) =# CREATE USER djangouser ;
* 	e) =# ALTER USER djangouser WITH PASSWORD 'djangopassword' ;
*       f) =# CREATE DATABASE djangodb OWNER djangouser ;
*	g) =# GRANT ALL PRIVILEGES ON DATABASE djangodb TO djangouser WITH
*	      GRANT OPTION ;
*	h) =# \q ;
*	i) Chiudere il terminale di postgres -> $ exit
*
*
* 2) SETUP DEL PROGETTO
*    Da linea di comando:
*	a) Spostarsi all'interno della cartella di progetto 'ProgettoLD'
*	b) Inizializzare il database -> $ python manage.py makemigrations
*	c) Applicare le migrazioni -> $ python manage.py migrate
*	d) Creare un admin per il sito -> $ python manage.py createsuperuser
*	e) (*Opzionale) Popolare il database -> $ python manage.py sampledata
*	   Questo comando permette di provare fin da subito tutte le
*	   funzionalità di Orariolezioni, con un discreto numero di dati.
*	f) (*Opzionale) Creare un utente di prova -> 
*			$ python manage.py newuser [chiave di registrazione]
*	   Di base vengono fornite queste chiavi di registrazione, ma l'admin
*	   creato al punto d) può cambiarle alla sezione 'Docenti' nel
*	   pannello di amministrazione:
*	   -------------UTENTE PREDEFINITO------CHIAVE DI REGISTRAZIONE--------
*
*			StefaniaStatis		OWUE5
* 			StefanoStati		9UEBR
*			AntonioAntani		P5WE9
*			FabrizioFarmaci		N0782
*			JohnDoe			097S8
*			IgnazioInforma		08BC3
*			AnnaLisi		2I38B
* 			MatteoMatico		C3N9N
*			AldoGebra		NDCWW
*			PippoProgrammi		MQD3I
*			SistoTemi		MAHD2
*			MargaretThatcher	X923U
*	   --------------------------------------------------------------------
*	   Ognuno di questi utenti sample ha password 'nuovoutente' ed è
*	   assegnato a un docente. E' possibile quindi loggare su Orariolezioni
*	   con uno di questi account e testare anche l'orario personale.
*
*
* 3) AVVIO DELL'APPLICAZIONE
*    Da linea di comando:
*	a) Spostarsi all'interno della cartella di progetto 'ProgettoLD'
*	b) Avviare il server -> $ python manage.py runserver
*
*******************************************************************************
