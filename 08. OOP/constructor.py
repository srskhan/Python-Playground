class Pen:

    def __init__(self, brand, origin, price):
        self.brand = brand
        self.origin = origin
        self.price = price

p1 = Pen("Matador", "BD", 5)
p2 = Pen("All Time", "BD", 6)
print(p1.brand, p1.origin, p1.price)
print(p2.brand, p2.origin, p2.price)
