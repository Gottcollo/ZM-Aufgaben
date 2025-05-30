class Konto:
    def __init__(self):
        self.kontoinhaber = None
        self.kontostand = 0.0

    def einzahlen(self, betrag):
        self.kontostand += betrag
    
    def abheben(self, betrag):
        try:
            if betrag <= self.kontostand:
                self.kontostand -= betrag
            else:
                print('Zu wenig Geld auf dem Konto.')
        except ValueError:
            print('Fehler bei der eingabe') 
    def zeige_kontostand(self):
        print(F'{self.kontostand} € hast du im Konto')

