
class Person:
    def __init__(self):
        self.name = "Poonam"
        self.__age = 23
        self.__address = "Pune"
    def display(self):
        print("Person name=",self.name)
        print("Person address=",self.__address)
        print("Age of the person=",self.__age)


obj = Person()
obj.display()

print(obj.name)
print(obj._Person__address) #to access the private variable name mangling is required
print(obj._Person__age)


import sys
sys.exit()

class Person:
    def __init__(self):
        self.name = "Poonam"
        self.__age = 23
        self.address = "Pune"


obj=Person()
print("Person name=",obj.name)
print("Person address=",obj.address)
print("Age of the person=",obj.age)


import sys
sys.exit()

class Person:
    def __init__(self):
        self.age = 23


obj=Person()
print("Age of the person=",obj.age)


import sys
sys.exit()

class Person:
    def __init__(self):
        self.__age = 23


obj=Person()
print("Age of the person=",obj.age)

