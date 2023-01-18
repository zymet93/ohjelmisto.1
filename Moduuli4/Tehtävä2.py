
jatkuu = True

while jatkuu:
    tuuma = int(input("Anna tuumat: "))
    cm = tuuma * 2.54
    print(cm)
    if tuuma < 0:
        jatkuu = False