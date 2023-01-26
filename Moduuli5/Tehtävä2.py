# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

luvut = []
jatkuu = True
while jatkuu:

    luku = input( 'Anna luku: ')
    print(luku)

    if luku =='':
        jatkuu = False
        print("5 suurinta lukua ovat:", luvut[0:5])
    else:
        luvut.append(int(luku))
        luvut.sort(reverse=True)