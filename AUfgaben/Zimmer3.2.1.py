print('Gib dein Zimmer an!')

zimmernummer = input('Jetzt erstmal deine Zimmernummer')
zimmergröße = input('Wie Groß ist es?')
fensteranzahl = input('Wieviele Fenster hat es?')
etage = input('In welchem Stockwerk ist dein Zimmer?')
zimmerpreis = input('Wieviel ist das Zimmer pro Monat wert?')
zimmerart = input('Wie nutzt du das Zimmer? Als Botanikzimmer, technikzimmer oder Schlafzimmer?')
bodenbelag = input('Was ist auf deinem Boden ausgelegt?')
balkon = input('Besitzt das Zimmer ein Balkon?')
himmelsrichtung = input('In welcher Richtung liegt das Zimmer?')
wlan = input('Ist Wlan existent im Zimmer?')

print(F'''Lass mich das wiederholen. 
      Deine Zimmernummer ist {zimmernummer} und dein Zimmer ist {zimmergröße}m² groß.
      Du hast {fensteranzahl} Fenster und dein Zimmer ist in der Etage {etage}.
      Dein Zimmer kostet dich {zimmerpreis} und du nutzt das Zimmer als {zimmerart}.
      Dein Bodenbelag ist {bodenbelag}. 
      Das Zimmer ist in richtung {himmelsrichtung}.
      Balkon = {balkon}
      Wlan = {wlan}''')