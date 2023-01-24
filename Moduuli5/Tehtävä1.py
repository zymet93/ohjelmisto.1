#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random
nopat = int(input("Syötä arpakuutioiden määrä: "))
lista = []
for n in range(nopat):
    noppa = random.randint(1, 6)
    lista.append(noppa)

summa = sum(lista)
print(summa)