def Aggiunta (lista_archivio):
    
    print("Inserisci il titolo del libro da aggiungere:")
    libro = input()
    if libro not in lista_archivio:
        lista_archivio.append(libro)
    else:
        print("Il libro è già presente nell' archivio")
    return lista_archivio



        
def Prestito_libro(lista_libreria):

    libro_prestito = input("Inserire il libro che si vuole prendere in prestito")
    return libro_prestito
   
def Riporta_libro():

    libro_restituito = input("Inserire il libro che si vuole restituire")
    return libro_restituito

def Archivio_libri_prestati(libro,lista_prestiti):
    lista_prestiti.append(libro)
    return lista_prestiti


def Disponibilità_prestito(libro,lista_archivio,lista_prestiti):
    if libro in lista_archivio and libro not in lista_prestiti:
        print("Il libro è disponibile")


