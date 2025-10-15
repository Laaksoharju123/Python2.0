#kysytään käyttäjältä arpakuutioiden lkm
import random
nopat = int(input("arpakuutioiden lukumäärä:"))
heitto = 0
for x in range(0,nopat):
    heitto= heitto + (random.randint(1,6))
print(heitto)

