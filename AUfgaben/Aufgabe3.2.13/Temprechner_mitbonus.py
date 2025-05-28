def celsius_fahrenheit(c):
    return c * 9 / 5 + 32
def fahrenheit_celsius(f):
    return (f - 32) * 5 / 9

print('=' * 40)
print('   Temperaturenrechner')
print('=' * 40)
while True:
    print('=' * 40)
    print('   Temperaturrechner') #fake menü weil keine echte GUI
    print('1: Celsius zu Fahrenheit')
    print('2: Fahrenheit zu Celsius')
    print('4: Beenden')
    print('=' * 40)
    wahl = input('Wähle aus  ')
    print('=' *40)

    if wahl == '1':
        try:
            celsius = float(input('Gib die Celsiuszahl ein '))
            fahrenheit = celsius_fahrenheit(celsius)
            print(F'Bei {celsius} °C umgerechnet ist es {fahrenheit:.2f} °F')
        except ValueError:
            print('Keine gültige Eingabe. Nur die Zahl eingeben.')
    elif wahl == '2':
        try:
            fahrenheit = float(input('Gib die Fahrenheitzahl ein '))
            celsius = fahrenheit_celsius(fahrenheit)
            print(F'Bei {fahrenheit} °F umgewandelt ist es {celsius:.2f} °C')
        except ValueError:
            print('Keine gültige Eingabe. Nur die Zahl eingeben. ')
    elif wahl == '4':
        print('   Gute Auswahl! Bye Bye.')
        break
    else:
        print('Das war keine Auswahlmöglichkeit')

print('=' * 40)
print('Ich schalte mich nun ab!')
print('=' * 40)