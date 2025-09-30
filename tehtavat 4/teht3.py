
syote = input("Anna luku: ")

if syote != "":
    luku = float(syote)
    pienin = luku
    suurin = luku

    syote = input("Anna luku: ")
    while syote != "":
        luku = float(syote)
        if luku < pienin:
            pienin = luku
        if luku > suurin:
            suurin = luku
        syote = input("Anna luku: ")

    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")

else:
    print("Et antanut yhtään lukua.")
