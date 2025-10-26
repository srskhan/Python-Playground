#abstract base class
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod     #enforce all child class to have same method.
    def eat(self):
        print("Give me food")

    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self):
        super().__init__()

    def eat(self):
        print("Give me banana!")

    def move(self):
        pass

mon = Monkey()
print(mon.eat())
