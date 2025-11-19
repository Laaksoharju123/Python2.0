
vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")
(eka, toka, kolmas, neljas) = vuodenajat

kk = int(input("Anna kuukauden nro(1-12):"))

if kk == 12 or kk == 1 or kk == 2:
    print(eka) #talvi

elif kk == 3 or kk == 4 or kk == 5:
    print(toka) #kevät

elif kk == 6 or kk == 7 or kk == 8:
    print(kolmas) #kesä

elif kk == 9 or kk == 10 or kk == 11:
    print(neljas) #syksy





