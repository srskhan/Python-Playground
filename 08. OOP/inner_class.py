class Color:
    def __init__(self):
        self.name = "Green"
        self.lg = self.LightGreen()

    def show(self):
        print("Name:", self.name)

    class LightGreen:
        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print('Name:',self.name)
            print('Code:',self.code)

c = Color()
c.show()
i = c.lg
i.display()