#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

nopan_tahkot = int(input("Syötä nopan tahkojen määrä: "))


def noppa():
    return random.randint(1, nopan_tahkot)

while True:
    x = noppa()
    print(x)
    if x == nopan_tahkot:
        break