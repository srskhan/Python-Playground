class Calculator:
    brand = 'Casio MS991'

    def add(self, num1,num2):
        sum = num1+num2
        return sum
    

cal = Calculator()
print(cal.add(5,6))