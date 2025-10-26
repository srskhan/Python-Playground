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

    def __add__(self, others):
        return self.age + others.age
    
    def __gt__(self, other):
        return self.age > other.age

amla = Cricketer("Hasim Amla", 40, 70, 85, "SA")
musi = Cricketer("Mushfiqur Rahman", 38, 65, 75, "BD")
print(amla+musi)
print(amla > musi)