#Encapsulation

class Base: 
    def __init__(self): 
        self.__a = 2

class Derived(Base): 
    def __init__(self): 
  
        Base.__init__(self) 
        print("Calling protected member of base class: ",  
              self.__a) 
        
        self._a = 3
        print("Calling modified protected member outside class: ", 
              self._a) 
  
obj1 = Derived() 
obj2 = Base()

#To access the private member in encapsulation
# class Base: 
#     def __init__(self): 
#         self.__a = 2

# class Derived(Base): 
#     def __init__(self): 
  
#         Base.__init__(self) 
#         print("Calling protected member of base class: ",  
#               self._Base__a) 
        
#         self._a = 3
#         print("Calling modified protected member outside class: ", 
#               self._a) 
  
# obj1 = Derived() 
# obj2 = Base()
