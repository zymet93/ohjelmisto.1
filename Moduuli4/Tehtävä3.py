# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
lista = []
while True:
    luku = input("Syötä luku: ")
    if luku == "":
        break
    lista.append(float(luku))

print("Pienin luku: " + str(min(lista)))
print("Suurin luku: " + str(max (lista)))