sex = input("mikä on sukupuolisi ? (M/N) ").capitalize()
hemoglobin = int(input("Mikä on hemoglobiiniarvosi? (g/l)? "))

if sex == "M".capitalize():
    if  hemoglobin>=134 and hemoglobin <=195 :
        print("Normaali hemoglobiini.")
    else:
        print("ei Normaali hemoglobiini.")
elif sex == "N".capitalize():
    if hemoglobin>= 117 and hemoglobin <= 175:
        print("Normaali hemoglobiini.")

    else:
        print("ei normaali hemoglobiini.")
else:
    print("Virheellinen syöte!")