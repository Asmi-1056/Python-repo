#Super Keyword

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Branch(Student):
    def __init__(self, name, id, branch):
        super().__init__(name, id)
        self.branch = branch

i = Branch('Asmi', 1056, 'CSE')
print(i.name)
print(i.id)
print(i.branch)