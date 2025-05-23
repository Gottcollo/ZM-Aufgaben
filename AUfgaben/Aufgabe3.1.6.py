name = "Max Mustermann"
alter = 30
geschlecht = "männlich"
groesse = "1,80m"
gewicht = "75kg"
augenfarbe = "braun"
haarfarbe = "schwarz"
beruf = "Softwareentwickler"
hobby = "Lesen"
charakter = "freundlich"
#der gegebene Datensatz jetzt in ein Satz umwandeln
print(F'''{name} ist ein {alter} jähriger, {charakter}er {geschlecht}er mit {augenfarbe}en Augen und {haarfarbe}en haaren, 
      {groesse} groß und {gewicht} Gewicht, der als {beruf} arbeitet und sein hobby ist {hobby}.''')
#erfolgreiche ausgabe auch wenn der Detusche Satz grammatikalisch richtig war fühlt er sich falsch an.
#hier fängt mein Datensatz an
player1 = 'Sam'
player2 = 'Sam2'
player1gender = 'männlich'
player2gender = 'männlich'
ballert = 'trifft'
life = 'leben'
treffer = 2
getroffen = 1
print(F'{player1} schlägt {treffer} mal {player2} und {ballert} {getroffen} mal sein kopf und nimmt ihm das {life}  ')
#hat funktioniert und ich kann nun print(F'...') anwenden um eine gesamte ausgabe zu machen/das was ich bei meinem ersten teil nicht konnte