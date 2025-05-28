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
    kleinste = zahlen[0] #min oder max etwas als variable zu nenne zerstört die funktionen min und max von python
    groesste = zahlen[0]
    summe = 0

    for zahl in zahlen:
        if zahl < kleinste:
            kleinste = zahl
        if zahl > groesste:
            groesste = zahl
        summe += zahl

    durchschnitt = summe / len(zahlen)

    sortiert = sorted(zahlen)
    #zahlen.sort()  geht auch hab ich später gefunden. dadurch keine neue liste erstellt sondern alte sortiert
    
    print(f"Die größte Zahl ist {groesste}")
    print(f"Die kleinste Zahl ist {kleinste}")
    print(f"Der Durchschnitt der Zahlen ist {durchschnitt}")
    print(f" Eine Sortierte Liste {sortiert}")
else:
    print("Keine Zahlen eingegeben.")

