zahlenstrahl = [4, 7, 2, 9, 1, 5, 3,]

#erster teil
print(F'Die Länge der liste: {len(zahlenstrahl)}')
print(F'Maximale Zahl: {max(zahlenstrahl)}')
print(F'Minimalste Zahl: {min(zahlenstrahl)}')
#erster test ging alles gut

#gibt es eine funktion für denn durchschnitt?
#Der Durchschnitt ist die Summe aller Zahlen geteilt durch die Anzahl der Zahlen – nicht einfach durch 2.
durchschnitt = sum(zahlenstrahl) / len(zahlenstrahl)
print(F'Der Durchschnittliche wert beträgt: {durchschnitt}')
#sollte wohl auch vorwärts zeigen um ein rückwärts zu zeigen
print(F'Vorwärts {zahlenstrahl}')
print(F'Rückwärts {list(reversed(zahlenstrahl))}') #zahlenstrahl.reverse() ging nicht und hat mir wert NULL ausgegeben

#habe hilfe gebraucht für die for klausel internetsuche hat geholfen
#Modulo hier bei 'Zahl' kann ich andere variablennamen wählen 
#zahl gewählt weil das ein zahlenstrahl ist und das logisch also zahlen sind
geradezahlen = [zahl for zahl in zahlenstrahl if zahl % 2 == 0]
print(F'der neue Zahlenstrahl: {geradezahlen}')

print(f'Neue Liste: {list(filter(lambda n: n % 2 == 0, zahlenstrahl))}')