class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'Item': item, 'Price': price, 'Quantity': quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            total+= item['Price']* item['Quantity']

        if( amount> total):
            print(f"Here is your item and extra money {amount - total} tk")
        elif (total > amount):
            print(f" You have to pay more {total- amount} tk")
        else:
            print(f"Payment Exact. Thanks for shopping.")

piku = Shopping('Priyash')
piku.add_to_cart('Beef', 800, 1)
piku.add_to_cart('Egg', 55,2)
piku.add_to_cart('Rice',90,5)
piku.checkout(2000)
