note = int(input('Gib deine Note an und ich sage dir was sie Sprachlich ist.'))

if note == 1:
    print('Sehr gut')
elif note == 2:
    print('Gut')
elif note == 3:
    print('Befriedigend')
elif note == 4:
    print('Ausreichend')
elif note == 5:
    print('Mangelhalft')
elif note == 6:
    print('Ungenügend')
else:
    print('Gibt es nicht als Endnote!')
print(F'Ich hoffe du bist zufrieden mit deiner {note}')