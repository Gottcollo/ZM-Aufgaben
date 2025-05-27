import random

print('Ich denke mir eine Zahl zwischen 1 und 100. Du musst sie erraten um dich zu befreien.')
print('Es sind nur Ganze Zahlen an die ich denke!')

zahl = random.randint(1, 100)
versuche = 0
ratezahl = False 

while not ratezahl:  #while sagt immer (wenn es wahr ist) while not sagt wenn es nicht wahr ist
    try:                #marius hat mir ein tipp gegeben
        wette = int(input('Du sagst welche Zahl?'))
        versuche += 1

        if wette < 1 or wette > 100:
            print('Ich sagte zwischen 1 udn 100')

        elif wette < zahl:
            print('Du musst höher gehen.')
        elif wette == zahl:
            print(F'Genau richtig! Du hast nur {versuche} versuche gebraucht')
            ratezahl = True
        else:
            print('Das ist zu hoch')
    
    except:
        print('Ich sagte Ganze Zahlen.')