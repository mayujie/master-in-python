# https://www.youtube.com/watch?v=Owr_JtcjMAw&ab_channel=BrendanMetcalfe

class Car:
    def my_instance_method(self):
        return "my_instance_method!!", self

    @classmethod
    def my_class_method(cls):
        return "class_method!!", cls

    @staticmethod
    def my_static_method():
        return "static_method!!"


if __name__ == "__main__":
    c = Car()
    print(c)
    print(c.my_instance_method())
    print(c.my_class_method())
    # staticmethod you don't need the self or cls, you don't really need to access it
    # you don't need to access the instance of the car or car itself
    print(c.my_static_method())
