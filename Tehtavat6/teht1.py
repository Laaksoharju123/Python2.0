#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
# nopan silmäluvun väliltä 1..6.
#Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
#Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def heittaa(tahkot):
    return random.randint(1,tahkot)

tulos=0
#pääohjelma
#ohjelma kysyy montako tahkoa nopassa on ja sitten maksimi silmälukua.
tahkot=int(input("kuinka monta tahkoa nopassa on?:"))
maksimi=int(input("mikä on maksimi silmäluku?"))

#looppi pyörii niin kauan kun se heittää annetun maksimi määrän.
while tulos !=maksimi:
    tulos = heittaa(tahkot)
    print(f"määrä: {tulos}")

#muokattu edellinen ohjelma eli tehtävät 1-2 tässä.
