#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.

x = 1
while x < 1000:
    if (x%3)==0:
        print("Jaollinen luku" ,x )
    x+=1