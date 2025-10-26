class Bank():
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        print(self.balance)
    
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self, amount):
        if(amount<self.min_withdraw):
            print(f"You cann't withdraw less than {self.min_withdraw}.")
        elif(amount> 100000):
            print(f"You cannot withdraw more than {self.max_withdraw}")
        else:
            self.balance-=amount
            print(f"Here is your amount {amount}")
            print(f"You have total {self.balance}")

dbbl = Bank(15000)
dbbl.deposit(5000)
dbbl.get_balance()
dbbl.withdraw(90)
dbbl.withdraw(500000)
dbbl.withdraw(1000)

