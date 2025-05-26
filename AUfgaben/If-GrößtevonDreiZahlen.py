print('Gib mir deine drei Zahlen und ich sage dir welche die größte ist.')
zahl1 = float(input("Deine erste Zahl?"))
zahl2 = float(input("Deine zweite Zahl?"))
zahl3 = float(input("Deine dritte Zahl?"))

#ich fake das zahl1 die größte zahl ist und überprüfe und ersetze falls es stimmt.
#ich wollte einfach eine überprüfung umgehen das geht aber nicht.
#fehler bemerkt ich muss die größte zahl ersetzen damit es sinn ergibt. Ein zusatzwert als Platzhalter für Groß

groesste = zahl1 #placeholder gefüttert

if zahl2 > groesste:
    groesste = zahl2

if zahl3 > groesste:
    groesste = zahl3

#alles ausgeben damit man seine alten zahlen auch sieht
print(F'''Von deinen drei Zahlen {zahl1}, {zahl2} und {zahl3}. Ist {groesste} die größte Zahl.
       War nur ein wenig kompliziert mit einem Placeholder''')
