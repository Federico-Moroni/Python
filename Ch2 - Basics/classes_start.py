
#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

from operator import truediv


class vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
        self.color = "rojo"

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

    def wash(self, is_washed):
        self.is_washed = is_washed


class car(vehicle):
    def __init__(self, enginetype):
        super().__init__("car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)


class motorcycle(vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)


class sport(car):
    def __init__(self, brand, top_speed):
        super().__init__("sport")
        self.brand = brand
        self.top_speed = top_speed

    def wash(self, is_washed):
        super().wash(is_washed)
        print("Your car was succesfully washed")


car1 = car("gas")
car2 = car("electric")
mc1 = motorcycle("gas", True)
sport1 = sport("Ferrari", 350)
