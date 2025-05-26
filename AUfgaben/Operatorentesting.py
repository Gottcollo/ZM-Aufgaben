value1 = float(input('gib deine erste zahl an: '))#hier ein typecast zu float
value2 = float(input('deine zweite zahl: '))#typecast zu float damit kein str beginnt

print(value1 + value2)#check ob es richtig rechnet
print('Boolcheck beider werte')
print(value1 == value2)#hier auf glecihehit überprüft
print('jetzt ein typecheck bei 3<=5 ')
print(type(3<=5))#hier ein typecheck
print(3<=5)
print('Value3 check geteilt durch 2')#hier ein dritten value hergestellt und es mit value3 / 2 ausgeben
value3 = value1 + value2
value3 /= 2
print(value3)
