print('Ich überprüfe für dich ob deine Zahl +, -, oder null ist.')
zahl = float(input('Gib mir die Zahl!'))

if zahl < 0:
    print('Negative Zahl')
elif zahl > 0:
    print('Positive Zahl')
else:
    print('NULL')

print(F'Da hast du deine {zahl}')