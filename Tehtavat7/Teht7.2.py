
nimet = set()
while True:
    nimi=input("anna nimi")
    if nimi == "":
        break
    if nimi in nimet:
        print("aiemmin syötetty nimi")
    else:
        print("uusi nimi")
        nimet.add(nimi)
for n in nimet:
    print(n)