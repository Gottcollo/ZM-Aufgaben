zahlen = []   #eine leere liste die ich passiv fühlen will 

while True:
    userinput = input('Gib eine Zahl ein oder "stopp" zum Beenden')
    if userinput.lower() == 'stopp':
        break
    try:
        zahl = int(userinput) #für denn Bonus später jetzt schon INT anstatt Float
        zahlen.append(zahl) #append fügt einfach ein element hinzu 
                            #hier lass ich die zahl die der user gibt einfügen in die liste
        min = zahlen[0]
        max = zahlen[0]
        summe = 0

        for zahl in zahlen:
            if zahl < min:
                min = zahl
            if zahl > max:
                max = zahl

            summe += zahl

        durchschnitt = summe /len(zahlen) #schon in listenzahlen genutzt
        sortiert = sorted(zahlen)  #sorted ist eine funktion zum sortieren von INT

        print(F'Maximale Zahl ist {max}')
        print(F'Minimalste Zahl ist {min}')
        print(F'Ein Sortierter Zahlenstrahl {sortiert}')
        print(F'Noch mehr?')

    except ValueError: #try und except sind schwer zu meistern
        print('Das war wohl keine Ganzzahl')

