print('Spielen wir Gerade und ungerade')
zahl = int(input('Gib eine ganze Zahl ein und ich checke ob es Gerade oder ungerade ist! '))

#if klausel mit Modulo das checkt rest und nicht die zahl selbst (%) 
#ist etwas teilbar durch zwei ohne rest ist es Gerade!
if zahl % 2 == 0:
    print('Die Zahl ist gerade.')
else:
    print('Die Zahl ist ungerade.')
