

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def parittomat(lista):
    uusi = []
    for luku in lista:
            if luku % 2 == 0:
                uusi.append(luku)
    return(uusi)

#pääohjelma

uusi_lista = parittomat(lista)
print("Alkuperäinen lista:", lista)
print("Parilliset luvut:", uusi_lista)
