grenzwert = int(input('Bis zu welcher Ganzzahl willst du rechnen?'))

summe = 0
for zahl in range(1, grenzwert + 1):#ein zahlenstrahl von 1 bis X erstellen und user gibt 
                                    #grenzwert an +1 weil sonst wird der grenzwert nicht benutzt
    if zahl % 2 == 0: #if schleife stopft das rein
        summe += zahl #plus rechnen auf die summe


print(F'Die Summe von 1 bis {grenzwert} beträgt {summe}!')