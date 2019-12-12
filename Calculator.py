#This is an excercise program for a text based calculator using class and inheritance.
class Math:
    num1 =  0.00
    num2 =  0.00
    result = 0.00
    fun ="None"
    def __init__(self):
        a = int(input("Enter first number : "))
        b = int(input("Enter Second number : "))
        self.num1 = a
        self.num2 = b
    def showResult(self):
        print(self.fun, " of ", self.num1, " and ",self.num2, " is ", self.result)
class Add(Math):
    def __init__(self):
        self.fun = "Addition"
        Math.__init__(self)
        self.result=self.num1+self.num2
        self.showResult()
class Mul(Math):
    def __init__(self):
        self.fun = "Product"
        Math.__init__(self)
        self.result=self.num1*self.num2
        self.showResult()
cal1 = Add()
cal2 = Mul()



