# Classes
# Methods are fuctions associated with a class

import datetime
from calendar import weekday


class Employee:

    # class atribute or class variable
    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    # method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static methods. Used when it has nothing to do with my instance or class variables
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# This is called to instantiate 3 employees
emp1 = Employee('Federico', 'Moroni', 50000)
emp2 = Employee('Rocio', 'Moroni', 60000)
emp3 = Employee('Natalia', 'Ribero', 55000)
# emp_str_4 = 'Andres-Ashllian-42000'
# new_emp_4 = Employee.from_string(emp_str_4)

# Employee.set_raise_amt(1.08)
# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)

my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
