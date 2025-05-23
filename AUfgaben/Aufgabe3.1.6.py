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