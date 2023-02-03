#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien
# lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

maakoodi = input("Kirjoita maakoodi: ")
sql = "SELECT type, count(*) FROM airport WHERE iso_country = '" + maakoodi + "' GROUP BY type"
cursor = yhteys.cursor()
cursor.execute(sql)
tulos = cursor.fetchall()
for rivi in tulos:
    print("Lentokenttätyyppiä", rivi[0], rivi[1], "kappaletta.")