print('Du willst dein BMI wissen?')

gewicht = float(input('Körpergewicht in KG bitte.'))
groesse = float(input('Wie Groß bist du in M bitte (1.75) als Beispiel'))

#bmi berechnet man nach dem internet genau so!
bmi = gewicht / (groesse ** 2)

print(F'Dein BMI beträgt: {bmi}')
print(F'und du bist lass mich kurz checken.')

if bmi < 18.5:
    print('Du bist untergewichtig. Mach was dagegen!')
elif 18.5 <= bmi < 25:
    print('Du hast Normalgewicht. Gut für dich.')
elif 25 <= bmi < 30:
    print('Du bist übergewichtig. Willst du das?')
else:
    print('Adipositas nachdem Internet. Geh sofort raus und MACH WAS DAGEGEN.')