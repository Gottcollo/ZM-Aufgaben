class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None

car1 = Car()
print(car1.car_brand)
car1.car_brand = 'Audi'
car1.horse_power = 255
car1.color = 'Blau'
print(car1.car_brand)
print(car1.color)
print(car1.horse_power)

car2 = Car()
print(car2.car_brand)
car2.car_brand = 'BMW'
car2.horse_power = 255
car2.color = 'Schwarz'
print(car2.car_brand)
print(car2.color)
print(car2.horse_power)