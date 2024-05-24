# here we are dealing with object oriented programming working with classes and Objects
import random


class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.price = self.set_price(brand)

    def set_price(self, brand):
        if brand == 'Marcedenz':
            return '20 million'
        elif brand == 'Maluti':
            return '10 million'
        elif brand == 'Toyota':
            return '14 million'
        else:
            return '25 million'

    def display(self):
        print(f'Car Brand: {self.brand}, Color: {self.color}, Price: {self.price}')


# List of colors and brands
colors = ['Blue', 'Red', 'Green', 'Black']
brands = ['Marcedenz', 'Maluti', 'Toyota', 'Tesla']



random.shuffle(colors)
# Create and print car objects
cars = []

for i in range(len(colors)):
    car = Car(colors[i], brands[i])
    cars.append(car)
    car.display()
