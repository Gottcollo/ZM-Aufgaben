class Konto:
    def __init__(self,kontoinhaber):
        self.kontoinhaber = kontoinhaber
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
        print(F'{self.kontostand} € hast du im Konto. {self.kontoinhaber} ist der Bankkontoinhaber.')

konto1 = Konto('Sam')
konto1.einzahlen (200)
konto1.abheben(50)
konto1.zeige_kontostand()
