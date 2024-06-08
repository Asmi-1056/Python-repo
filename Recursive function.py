#Recursive function  
         
list=['Mango','Peach','Watermelon','Cherry','Jackfruit','Peach','Lichi']
i=0
def Fruit(name,list,i):
     i1=i
     if list[i] == name:
         print('found at index ',i)
     else:
         i1=i1+1
         Fruit(name,list,i1)
Fruit('Cherry',list,0)