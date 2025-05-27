age = int(input('Gib hier dein Alter an!')) #hier eine If-else-elif-Klausel getestet

if age < 18:
    print('Bursche jetzt geh aber raus spielen, ja!')
    print('Wir sehen dich!')
    age = 18
    print(F'Du musst {age} alt sein!')
elif age == 18:
    print(F'Wir wissen du bist Erwachsen, aber bist du wirklich bereit?')
else:
    print('Du bist volljährig sehr gut.')
print('Ende') #ende des Klausel test nummer 2