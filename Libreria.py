import libro


lista_archivio = []
lista_prestiti = []

while True:
    
    if len(lista_archivio) == 0:
        print("La libreria è vuota. Aggiungi il primo libro")
        lista_archivio = libro.Aggiunta(lista_archivio)
    else:
        print("Selezionare cosa fare:")
        print("1) Aggiungere un libro\n2) Stampa a schermo la libreria\n3) Disponibilità libreria\n4) Libro in prestito")
        print("5) Restituzione\n6) Exit")
        scelta_funzione = int(input())
        if (scelta_funzione == 1):
            lista_archivio = libro.Aggiunta(lista_archivio)
        elif (scelta_funzione == 2):
            libro.Archivio(lista_archivio)
        elif(scelta_funzione==3):
            libro.Disponibilita_archivio(lista_archivio)
        elif (scelta_funzione==4):
            libro.prestito(lista_archivio,lista_prestiti)
            lista_archivio = libro.prestito[0]
            lista_prestiti = libro.prestito[1]
        elif (scelta_funzione==5):
            libro.restituzione(lista_prestiti)
            lista_archivio = libro.prestito[0]
            lista_prestiti = libro.prestito[1]
        elif(scelta_funzione==6):
            break