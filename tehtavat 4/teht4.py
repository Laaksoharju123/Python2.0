
import random
oikea_luku = random.randint(1,10)

arvaus = 1

while oikea_luku != arvaus:
    arvaus = int(input("Arvaa luku (1–10): "))

    if arvaus < oikea_luku:
        print("arvaus on liian pieni.")

    elif arvaus > oikea_luku:
        print("arvaus on liian suuri.")

    else:
        print("oikein.")
