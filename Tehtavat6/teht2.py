

def gallonat(gallonat):
    litrat = gallonat * 3.785
    return litrat

#pääohjelma
while True:
    määrä=float(input("kuinka monta gallonaa? "))

    if määrä < 0:
        print("ohjelma loppui")
        break

    litrat = gallonat(määrä)
    print(f"{määrä} gallonaa on {litrat} litraa")


