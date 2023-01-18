#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# #Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain
# jos ne ovat jaollisia myös neljälläsadalla.

import math
Vuosi = int(input("Anna vuosiluku : "))
if ((Vuosi % 400 == 0) or
        (Vuosi % 100 != 0) and
        (Vuosi % 4 == 0)):
    print("On karkausvuosi ");
# Jos ei ole karkausvuosi
else:
    print("Ei ole karkausvuosi ")