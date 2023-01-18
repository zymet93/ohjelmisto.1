#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin,
# tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).
password = "rules"
user = "python"
i = 1
while i <=5:

    nimi = input("Anna Käyttäjänimi: ")
    salasana = input("Anna salasana: ")

    if user == nimi:
        if salasana == password:
            print("Tervetuloa")
            break

        else:
            print("Pääsy evätty")
    else:
        print("Pääsy evätty")

    i+=1