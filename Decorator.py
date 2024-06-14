#Decorator 

def dec(func):
    def process():
        print("Welcome")
        func()
        print("Goodbye")
    return process
@dec
def yes():
    print('Asmi')
yes()
