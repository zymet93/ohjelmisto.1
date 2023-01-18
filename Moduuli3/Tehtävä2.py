#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka."""

hytti = input('Anna laivan hyttiluokka  ').capitalize()
if hytti == 'LUX'.capitalize():
    print('LUX on parvekkeellinen hytti yläkannella.')

elif hytti == 'a'.capitalize():
    print('A on ikkunallinen hytti autokannen yläpuolella.')

elif hytti == 'b'.capitalize():
    print('B on ikkunaton hytti autokannen yläpuolella.')

elif hytti == 'c'.capitalize():
    print('C on ikkunaton hytti autokannen alapuolella.')
else:
    print('Virheellinen hyttiluokka.')