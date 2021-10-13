import datetime

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    # each method within a class automatically takes the instance as first argument, we always call that self
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # going to create an new Employee

    @staticmethod
    def is_workday(day) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.num_of_emps)
print(emp_1.fullname())
print(Employee.fullname(emp_2))

print(Employee.raise_amount)
print(emp_1.raise_amount)
# emp_2.raise_amount = 1.05
print(emp_2.raise_amount)

Employee.set_raise_amount(1.06)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# alternative constructor
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)


my_date = datetime.date(2021, 10, 12)
print(Employee.is_workday(my_date))
print(new_emp_1.is_workday(my_date))
my_date = datetime.date(2021, 10, 16)
print(Employee.is_workday(my_date))
print(new_emp_1.is_workday(my_date))