def celsius_fahrenheit(c):
    return c * 9 / 5 + 32
def fahrenheit_celsius(f):
    return (f - 32) * 5 / 9

while True:
    print('Temperaturrechner') #fake menü weil keine echte GUI
    print('1: Celsius zu Fahrenheit')
    print('2: Fahrenheit zu Celsius')
    print('4: Beenden')
    wahl = input('Wähle aus  ')

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
        print('Gute Auswahl!')
        break
    else:
        print('Das war keine Auswahlmöglichkeit')