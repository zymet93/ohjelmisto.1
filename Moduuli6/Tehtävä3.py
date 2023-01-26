#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina,
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.

import math
def gallonat_litroina(gallonat):
    litrat = gallonat * 3.785412
    return litrat


while True:
    gallonat = float(input("Syötä bensiinin määrä gallonina: "))
    if gallonat < 0:
        break
    tulos = gallonat_litroina(gallonat)
    #print 2 desimaalin tarkkuudella
    print("Bensiinin määrä litroina: ", ("%.2f" % tulos))
