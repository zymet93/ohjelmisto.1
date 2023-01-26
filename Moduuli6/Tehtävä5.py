#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
# joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja,
# tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def poista_parittomat_funktio(numbers):
    return [x for x in numbers if x % 2 == 0]

numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = poista_parittomat_funktio(numerot)
print("Alkuperäinen lista: ", numerot)
print("Karsittu lista: ",result)