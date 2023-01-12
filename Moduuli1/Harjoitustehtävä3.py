#Kirjoita ohjelma, joka kysyy suorakulmion
# kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

import math
kanta = float(input("Anna suorakulmion kanta "))
korkeus = float(input("Anna suorakulmion korkeus"))
print(f"suorakulmion pinta ala on {kanta*korkeus}")
print(f"suorakulmion piiri on {kanta+korkeus+kanta+korkeus}")