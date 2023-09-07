class Box:
    def __init__(self,length,breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def display(self):
        print("Volume of box=",self.length*self.breadth*self.height)

box1= Box(5,3,2)
box1.display()

box2= Box(4,6,2)
box2.display()

print("Height of Box1=",box1.height)
print("Height of Box2=",box2.height)










import sys
sys.exit()
class Student:
    roll=101
    name='Sagar'
    age=23

    def display(cls):
        print(cls.roll)
        print(cls.name)
        print(cls.age)

stud1 = Student()
stud1.display()
print("Name of the student=",stud1.name)