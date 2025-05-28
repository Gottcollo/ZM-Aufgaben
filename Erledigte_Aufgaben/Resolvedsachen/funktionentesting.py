def say_hello(first_name, last_name):
    print('Hallo ' + first_name + ' ' + last_name)
    print('Willkomen zurück')

say_hello('DU', 'ich')
print('Test')

def counter():
    counter = 1
    while counter <= 100:
        print(F'Dein counter = {counter}')
        counter += 1

counter()