def Aggiunta (lista_archivio):
    
    print("Inserisci il titolo del libro da aggiungere:")
    libro = input()
    if libro not in lista_archivio:
        lista_archivio.append(libro)
    else:
        print("Il libro è già presente nell' archivio")
    return lista_archivio

def Archivio(lista_archivio):
    print("I libri in archivio sono:\n", lista_archivio)

def Disponibilita_archivio(lista_archivio):
    print("Inserire il titolo per vederne la disponibilità")
    libro_richiesto = input()
    Disponibile = False
    if libro_richiesto in lista_archivio:
        print("Il libro è disponibile\n")
        Disponibile = True
    else:
        print("Il libro non è disponibile.")
    return Disponibile

def prestito(lista_libri_disponibili,lista_prestiti):
    print("I libri disponibili sono\n",lista_libri_disponibili)
    print("Inserisci il libro da prendere in prestito")
    libro_prestito = input()
    
    return lista_libri_disponibili.remove(libro_prestito),lista_prestiti.append(libro_prestito)

def restituzione(lista_libri_disponibili, lista_prestiti):
    print("Inserire il titolo del libro da restituire",lista_prestiti)
    libro_da_restituire = input()
    return lista_prestiti.remove(libro_da_restituire),lista_libri_disponibili.append(libro_da_restituire)
    

    
