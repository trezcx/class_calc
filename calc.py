class Calculator():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
        print(self.num1 + self.num2)


calc = Calculator(int(input(": ")), int(input(": ")))
calc.add()