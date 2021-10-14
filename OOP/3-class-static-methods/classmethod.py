# https://www.youtube.com/watch?v=o2ZaCUr4GFI&t=1s&ab_channel=BrendanMetcalfe
class Car:
    def __init__(self, features):
        self.features = features

    def __repr__(self):
        return f'Car ({self.features})'

    @classmethod
    def truck(cls):
        return cls(['4x4', 'Big Tires'])

    @classmethod
    def sport(cls, package):
        if package == "SRT":
            return cls(['300hp', '2x4', 'Sport Tires'])
        if package == "Hemi":
            return cls(['500hp', '2x4', 'Racing Tires'])


newCar = Car("Highbeams")
print('newCar', newCar)

newCar = Car.truck()
print('newCar', newCar)

newCar = Car.sport("SRT")
print('newCar', newCar)

newCar = Car.sport("Hemi")
print('newCar', newCar)