#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja
# tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

def hae_lentokentat_maasta(icao):

   # sql = f"SELECT name FROM airport WHERE iso_country = '{maa}'"
    sql = f'SELECT ident, name, municipality FROM airport WHERE ident="{icao}" ;'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    return tulos

icao = input("Anna icao koodi: ")
lentokentat = hae_lentokentat_maasta(icao)


if lentokentat:
    print (lentokentat)
else :
    print (f'Lentoasema kooodilla {icao} ei löydy')