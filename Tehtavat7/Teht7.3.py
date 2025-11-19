
lentoasemat = {}

while True:
    print("Valitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta")
    valinta = input("Anna valinta: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.\n")

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi on:", lentoasemat[icao], "\n")
        else:
            print("Koodia ei löytynyt.\n")

    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break

    else:
        print("Virheellinen valinta.\n")



