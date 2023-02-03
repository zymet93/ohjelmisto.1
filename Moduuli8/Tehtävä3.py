# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy import distance
from geopy.distance import geodesic
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )


def get_two_icao_code2(icao_code1, icao_code2):
    sql = f"SELECT airport.latitude_deg,airport.longitude_deg FROM airport WHERE ident='{icao_code1}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result1 = cursor.fetchone()
    print("Ensimmäinen sijainti (leveysaste, pituusaste): ", result1)


    sql2 = f"SELECT airport.latitude_deg,airport.longitude_deg FROM airport WHERE ident='{icao_code2}';"
    cursor = yhteys.cursor()
    cursor.execute(sql2)
    result2 = cursor.fetchone()
    print("Toinen sijainti (leveysaste, pituusaste): ", result2)

    if (result1 == None) or (result2 == None):
        print("Ei tuloksia. Yritä uudelleen...")
    else:
        print("Niiden välinen etäisyys kilometreissä: ", geodesic(result1, result2).km, "km")


user_input1 = input("Anna ensimmäinen ICAO-koodi: ")
user_input2 = input("Anna toinen ICAO-koodi: ")
get_two_icao_code2(user_input1, user_input2)