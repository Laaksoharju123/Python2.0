print("valitse mitä komentoa haluat käyttää:\n A:yhteenlasku \n B:vähennyslasku"
      "\n C:kertolasku \n D:jakolasku")

valinta = input("valintasi A-D:")
a = float(input("anna ensinmäinen luku: "))
b = float(input("anna toinen luku: "))

if valinta == "A":
    print("yhteenlasku:", a + b)
elif valinta == "B":
    print("vahennyslasku:", a - b)
elif valinta == "C":
    print("kertolasku:", a * b)
elif valinta == "D":
    print("jakolasku:", a / b)
else:
    print("valintasi on virheellinen!")