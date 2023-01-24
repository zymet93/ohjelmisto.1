# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
import math

user_input = int(input("Syötä kokonaisluku: "))
if user_input <= 1:
    print(str(user_input) + " ei ole alkuluku.")
else:
    prime = True
    for i in range(2, int(user_input**0.5) + 1):
        if user_input % i == 0:
            prime = False
            break
    if prime:
        print(str(user_input) + " on alkuluku.")
    else:
        print(str(user_input) + " ei ole alkuluku.")