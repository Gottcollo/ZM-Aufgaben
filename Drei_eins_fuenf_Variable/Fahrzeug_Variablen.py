farbe = "Blau"
groesse = "Groß"
anzahl_tueren = "3 Tueren"
kraftstoffart = "Diesel"
fahrzeugtyp = "Lkw" #Was hat ein auto und ein LKW ? 
hersteller = "BMW"
baujahr = 2020
raeder = 6
Ladeflaeche_kg = 3500
getriebe = "Manuell"
print(f'Farbe = {farbe}')
print(F'Größe = {groesse}')
print(F'Anzahl an Türen = {anzahl_tueren}')
print(F'Tankt = {kraftstoffart}')
print(F'Fahrzeugtyp = {fahrzeugtyp}')
print(F'Der Hersteller ist {hersteller}')
print(F'Mit dem Baujahr {baujahr}')
print(F'Mit nur {raeder} Rädern')
print(F'Ladefläche stärke {Ladeflaeche_kg} in Stärke')
print(F'Das Getriebe ist {getriebe}')

#versuch zu swappen an werden innerhalb
print(F'Altes Baujahr {baujahr} und alte Stärke {Ladeflaeche_kg}')
baujahr, Ladeflaeche_kg = Ladeflaeche_kg, baujahr
print(F'Das soll nun das neue Baujahr sein {baujahr} und die neue stärke von der Ladefläche ist {Ladeflaeche_kg}')
#ES HAT FUNKTIONIERT
print('ICH HAB ES GETAUSCHT YUP YUP')