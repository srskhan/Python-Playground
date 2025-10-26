class Car:
    company = "Tesla"

    def __init__(self, model, color,price):
        self.model = model
        self.color = color
        self.price = price

car1 = Car('Model S', 'Red', 1500000)
car2 = Car('Cyber Truck', 'White', 5000000)
print(f'{car1.model}: Company - {car1.company} Price- {car1.price}')
print(f'{car2.model}: Company - {car2.company} Price- {car2.price}')

