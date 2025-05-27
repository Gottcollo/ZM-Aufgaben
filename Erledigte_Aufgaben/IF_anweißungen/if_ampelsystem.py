print('Ein Ampelsystemcheck')

#farbe einlesen // Frederick hat mich auf die idee gebracht man kann rot auch Rot schreiben oder ROT 
#versuch das es das mit überprüft. lower() macht alles in kleinbuchstaben
#strip() macht alle leerzeichen weg falls jemand leerzeichen am anfang nutzt.
farbe = input('Gib die Ampelfarbe ein (rot, gelb, grün): ').lower().strip()

#ifklausel bei kleingeschriebenes rot gelb und grün
if farbe == 'rot':
    print('KEINE BEWEGUNG!')
elif farbe == 'gelb':
    print('Noch nicht.')
elif farbe == 'grün':
    print('Rennen.')
else:
    print('Das war keine Farbe die ich kenne')
