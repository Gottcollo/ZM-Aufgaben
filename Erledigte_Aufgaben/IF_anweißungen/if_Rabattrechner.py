print('Rabattrechner für denn Kiosk')

einkaufspreis = float(input('Wieviel wurde bezahlt'))

#Rabatt berechnen und abziehen //multipliziert man den ursprünglichen Preis mit 0,10
if einkaufspreis > 100:
    rabatt = einkaufspreis * 0.10
    endpreis = einkaufspreis - rabatt
    print(f'Der Kunde bekommt 10% Rabatt ({rabatt} €).')
else:
    endpreis = einkaufspreis
    print('Kein Rabatt.')

# Endpreis ausgeben
print(f'Der zu zahlende Betrag ist: {endpreis} €')
