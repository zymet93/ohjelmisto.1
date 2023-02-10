#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee
# laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

x = int(input("Ilmoita kuhan pituus sentteinä: "))
if x < 37:
    print("Laske kuha takaisin järveen")
    print(f"{37-x} Senttiä alimmasta sallitusta pyyntimitasta")
else:
    print("Kuha on laillisen mittainen ")
