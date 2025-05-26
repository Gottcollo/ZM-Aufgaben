print('Willkommen beim Ratespiel. Ich denke mir drei Zahlen aus wenn nur eine von dir übereinstimmt dann gewinnst du ein Stern!')
print('Nur Zahlen von 1 bis 10!')
number1 = int(input('Ich denke an die Zahl?'))
number2 = int(input('Ich denke an die Zahl, aber erratest du Sie?'))
number3 = int(input('Ich denke jetzt an die letzte Zahl und die ist?'))

#gewinnzahl1 = 1
#gewinnzahl2 = 3
#gewinnzahl3 = 9

if number1 == 1 or number2 == 3 or number3 == 9: #or check ob es funktioniert
    print(F'Du hast richtig geraten!')
    print('DU HAST GEWONNEN, HURRAY!')
else:
    print('Kein Stern für dich. Tja so kann es sein!')

print('Vielen Dank für deinen Versuch!')