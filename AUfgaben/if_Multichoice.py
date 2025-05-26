print('A, B, C, oder D ob du richtig stehst kommt jetzt.')
#ist ein kinderspiel von mir gewesen als ich selbst ein Kind war

richtig = 'C'

#dank Frederik denke ich immer daran jetzt das bei Strings man vieles falsch machen kann
#also muss ich immer bei strings an .strip() und.upper() oder .lower() denken
antwort = input('Wo stehst du gerade? (A, B, C oder D): ').strip().upper()
#if_klausel check mit richtig 
if antwort == richtig:
    print(' Richtig! Du stehst RICHTIIIIIIG!')
else:
    print(' Falsch. Du bist RAUUUUUUUUS.')
