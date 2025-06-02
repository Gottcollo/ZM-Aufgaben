class Konto:
    def __init__(self,kontoinhaber):
        self.kontoinhaber = kontoinhaber
        self.kontostand = 0.0
        self.ueberziehungsrahmen = 100.00

    def einzahlen(self, betrag):
        self.kontostand += betrag
    
    def abheben(self, betrag):
        try:
            if  self.kontostand - betrag >= self.ueberziehungsrahmen:
                self.kontostand -= betrag
            else:
                print('Überziehungslimit überschritten.')
        except ValueError:
            print('Fehler bei der eingabe') 
    def zeige_kontostand(self):
        print(F'Konto von {self.kontoinhaber} - Kontostand: {self.kontostand:.2f} €')

    def zinsen_berechnen(self, zinssatz):
        if self.kontostand > 0:
            zinsen = self.kontostand * (zinssatz/100)
            self.kontostand += zinsen
            print(F'{zinsen:.2f} € wurden gutgeschrieben.')
        elif self.kontostand == 0:
            print(F'Keine Zinsen, weil dein Kontostand auf Null ist')
        else:
            print(F'Keine Zinsen, weil negativer Kontostand.')
    def __str__(self):
        return f'Konto von {self.kontoinhaber} - Kontostand: {self.kontostand:.2f} €'