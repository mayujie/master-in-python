# Basic concept
class Car:
    pass

# https://www.youtube.com/watch?v=AEOuYv699K4&ab_channel=BrendanMetcalfe
# Use @property decorator
class Car_1:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("**in the getter**")
        return self._name

    @name.setter
    def name(self, name):
        print("**in the setter**")
        if len(name) > 6:
            self._name = name

    @name.deleter
    def name(self, name):
        print("**in the deleter**")
        del self._name


class Car_2:
    def __init__(self, name):
        self._name = name

    def setname(self, name):
        print("**setname() called**")
        self._name = name

    def getname(self):
        print("**getname() called**")
        return self._name

    def delname(self):
        print("**delname() called")
        del self._name

    name = property(getname, setname, delname)


# Use property function

if __name__ == "__main__":
    my_car = Car()
    my_car.name = "Joey" # setter
    print("** my_car.name ** ", my_car.name) # getter

    print("\n case 1")
    my_car = Car_1("Jimmy")
    print("** my_car.name **", my_car.name)
    my_car.name = "JoeyJoy"
    print("** my_car.name **", my_car.name)

    print("\n case 2")
    my_car = Car_2("JIN")
    print("** my_car.name **", my_car.name)
    my_car.name = "JJ"
    print("** my_car.name **", my_car.name)
