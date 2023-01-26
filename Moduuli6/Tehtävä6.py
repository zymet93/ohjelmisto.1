#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

#pizzan halkaisija/hinta funktio
def pizza(halkaisija, hinta):
    pinta_ala = math.pi * (halkaisija /100 / 2) ** 2
    arvo = hinta / pinta_ala
    return arvo

#hinnat pääohjelma

hinta1 = float(input("Syötä 1. pizzan hinta euroina: "))
halkaisija1 = float(input("Syötä 1. pizzan halkaisija metreinä: "))
hinta2 = float(input("Syötä 2. pizzan hinta euroina : "))
halkaisija2 = float(input("Syötä 2. pizzan halkaisija metreinä: "))
summa1 = pizza(halkaisija1, hinta1)
summa2 = pizza(halkaisija2, hinta2)

#Printti 3 desimaalin tarkkuudella, muuten näyttää epäsiistiltä

print("Ensimmäisen pizzan hinta per neliö: ",f'{summa1:.3f}')
print("Toisen pizzan hinta per neliö: ",f'{summa2:.3f}')
if summa1 > summa2:
    print("2. pizzalla on alhaisempi yksikköhinta.")
elif summa2>summa1:
    print("1. pizzalla on alhaisempi yksikköhinta.")
# Jos sama hinta:
elif summa2==summa1:
    print(" Pizzoilla on sama yksikköhinta.")