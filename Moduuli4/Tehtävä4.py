# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen
# jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.


import math
import random

while True:

    luku = random.randint(1,10)
    luku1 = int(input("Arvaa luku: "))
    if luku1 == luku:
        print("Luku on oikein")
        break
    elif luku1 < luku:
        print("Liian pieni arvaus ")
    else:
        print("Liian suuri arvaus ")