#parent class
class Bird:
    print("Bird is ready")
    
#child class
class Penguin(Bird):
   def __init__(self):
       #call super() function
        super().__init__()
print("Penguin is ready")
        
peggy = Penguin()