#Parameterized Constructor
class five:
    def nine():
        print('Hello')

class new2:
    def __init__(self, n, r):
        print('This is a parameterized constructor')
        self.name = n
        self.r_no = r
    def call(self):
        print(f"{self.name}'s roll no is {self.r_no}")

b = new2('Asmi', 10)
b.call()
b.name = 'P'
b.r_no = 28
b.call()    
