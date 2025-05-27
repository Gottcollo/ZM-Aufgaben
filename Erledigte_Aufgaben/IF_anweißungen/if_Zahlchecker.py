print('Ich checke deine Zahlen, ob sie nacheinander folgen oder nicht.')

zahl1 = float(input('Deine erste zahl ist?'))
zahl2 = float(input('Die zweite zahl ist ?'))
zahl3 = float(input('Die letzte der zahlen?'))
if zahl1 < zahl2 < zahl3:
    print('ja die zahlen folgen aufeinander')
elif zahl3 < zahl2 < zahl1:
    print('ja die zahlen folgen aufeinander')
else:
    print('nein die zahlen folgen nicht aufeinander')

#denke hier ging eine Or sache jetzt nach dem lösen
#zahl1 = float(input('Deine erste zahl ist?'))
#zahl2 = float(input('Die zweite zahl ist ?'))
#zahl3 = float(input('Die letzte der zahlen?'))

#if (zahl1 < zahl2 < zahl3) or (zahl3 < zahl2 < zahl1):
#   print('Ja die zahlen folgen aufeinander')
#else:
#   print('nein die zahlen folgen nicht aufeinander')
