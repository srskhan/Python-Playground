class Person:
    def __init__(self,name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Rice, Polau, Beef")

    #force to override
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        super().__init__(name, age, height, weight)
        self.team = team

    #over ride method
    def eat(self):
        print("Vegetables, Fruits")

    def exercise(self):
        print("Exercise Regularly")

amla = Cricketer("Hasim Amla", 40, 70, 85, "SA")
print(amla.exercise())