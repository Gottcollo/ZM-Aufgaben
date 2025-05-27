zahlen = []   #eine leere liste die ich passiv fühlen will 

while True:
    userinput = input('Gib eine Zahl ein oder "stopp" zum Beenden')
    if userinput.lower() == 'stopp':
        break
    try:
        zahl = int(userinput) #für denn Bonus später jetzt schon INT anstatt Float
        zahlen.append(zahl) #append fügt einfach ein element hinzu 
                            #hier lass ich die zahl die der user gibt einfügen in die liste
    except ValueError:
        print('Das war wohl keine Ganzzahl')

if len(zahlen) != 0: #längencheck der liste sobald was drin ist gehts los
    minimum = zahlen[0]
    maximum = zahlen[0]
    summe = 0

    for zahl in zahlen:
        if zahl < minimum:
            minimum = zahl
        if zahl > maximum:
            maximum = zahl
        summe += zahl

    durchschnitt = summe / len(zahlen)

    # Liste sortieren (aufsteigend)
    zahlen.sort()
    
    print(f"Größte Zahl: {maximum}")
    print(f"Kleinste Zahl: {minimum}")
    print(f"Durchschnitt: {durchschnitt:.2f}")
    print(f"Sortierte Liste: {zahlen}")
else:
    print("Keine Zahlen eingegeben.")