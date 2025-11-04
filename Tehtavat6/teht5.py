import math
def yksikkohinta(halkaisija,hinta):
    sade = halkaisija / 200
    ala = 3.14159 * sade ** 2
    return hinta / ala


#pääohjelma
#kysytään käyttäjältä pizzat(halkasija ja hinnat

d1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
h1 = float(input("Anna ensimmäisen pizzan hinta (€): "))
d2 = float(input("Anna toisen pizzan halkaisija (cm): "))
h2 = float(input("Anna toisen pizzan hinta (€): "))

p1 = yksikkohinta(d1, h1)
p2 = yksikkohinta(d2, h2)

print(f"Ensimmäisen pizzan yksikköhinta on {p1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta on {p2:.2f} €/m²")

if p1 < p2:
    print("Ensimmäinen pizza on parempi vastine rahalle ")
elif p2 < p1:
    print("Toinen pizza on parempi vastine rahalle ")
else:
    print("Pizzat ovat yhtä hyviä vastineita rahalle!")
