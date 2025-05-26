print('Willkommen zu der Sternenausgabe! Treffe dreimal richtig und du gewinnst ein Stern!')
print('Nur Zahlen von 1 bis 49!')
number1 = int(input('Deine erste Zahl bitte!'))
number2 = int(input('Deine zweite Zahl bitte, Aufregend nicht wahr?'))
number3 = int(input('Deine letzte Zahl..... Mach mal schneller!'))

#gewinnzahl1 = 15
#gewinnzahl2 = 31
#gewinnzahl3 = 3

if number1 == 15 and number2 == 31 and number3 == 3:
    print(F'Du hast {number1}, {number2}, und {number3} in der Richtigen reihenfolge gesagt!')
    print('DU HAST GEWONNEN, HURRAY!')
else:
    print('Kein Stern für dich, Hurray!')

print('Vielen Dank für deinen Besuch!')