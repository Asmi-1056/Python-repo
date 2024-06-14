# Polymorphism

class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

class Car(Vehicle):
    def move(self):
        print('Move!')

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print('Fly!')

car1=Car('Mercedes','2014')
boat1=Boat('Speed','2019')
plane1=Plane('Fighter','2015')

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.year)
    x.move()
