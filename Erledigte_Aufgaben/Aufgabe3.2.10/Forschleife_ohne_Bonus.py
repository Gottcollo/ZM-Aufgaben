summe = 0
for zahl in range(1, 101): #einfach ein zahlenstrahl von 1 bis 100 machen
    if zahl % 2 == 0: #if schleife stopft das rein
        summe += zahl #plus rechnen auf die summe


print(F'Die Summe beträgt {summe}')