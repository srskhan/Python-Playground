class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []      # instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


Sadik = Shop('Sadik')
Sadik.add_to_cart('Watch')
Sadik.add_to_cart('PC')
print(Sadik.cart)

Fatu = Shop('Fatu')
Fatu.add_to_cart('Books')
Fatu.add_to_cart('Flowers')
print(Fatu.cart)
        