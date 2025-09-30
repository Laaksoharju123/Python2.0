
yritykset = 0

while yritykset < 5:
    kayttaja = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttaja == "python" and salasana == "rules":
        print("Tervetuloa!")
        break
    else:
        print("Väärä tunnus tai salasana.")
        yritykset += 1


if yritykset == 5:
    print("Pääsy evätty.")

