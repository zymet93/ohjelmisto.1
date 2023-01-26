#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.


def lista(numerot):
    return sum(numerot)
numerot = [3, 5, 6, 8, 10]
summa = lista(numerot)
print(summa)
