# Single Inheritance

"""class car:
    color = "Black"
    @staticmethod
    def start():
        print("cat started")

    @staticmethod
    def stop():
        print("car stop")

class ToyotaCar(car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car1.color)"""

# Multi-line Inheritance

"""class car:
    @staticmethod
    def start():
        print("cat started")

    @staticmethod
    def stop():
        print("car stop")

class ToyotaCar(car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()
print(car1)"""

# Multiple Inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)
# print(c1.varB)
# print(c1.varA)