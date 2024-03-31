class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name)


student1 = Student('jalal',15)

student1.printName()