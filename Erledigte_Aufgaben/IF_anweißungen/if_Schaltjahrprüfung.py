jahr = int(input('Welches Jahr willst du Überprüfen?'))

#komische Schaltjahrregel mit mathe erklärt mit and und or kombiniert alles in klammern setzen
#um es als eins anzuschauen.
if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):#Modulo(%) überprüft Rest nicht die rechnung selbst
    print(F'{jahr} ist ein Schaltjahr.')
else:
    print(F'{jahr} ist kein Schaltjahr.')

#ich denke ein elif wäre auch gegangen und zwar wie folgt:
#if (jahr % 4 == 0 and jahr % 100 != 0):
#   print(F'{jahr} ist ein Schaltjahr')
#elif (jahr % 400 == 0):
#   print(F'{jahr} ist ein Schaltjahr')
#else:
#   print(F'{jahr} ist kein Schaltjahr')
