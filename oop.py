# oop- Object oriented programming

class Student:
    #constructor method
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        #Member function
    def display(self):
        print(f"student name is : {self.name}, Age is : {self.age}, Score is : {self.score}")
#instance of the class(object)
myobj=Student("Robin",19,'A')
myobj.display()
myobj2=Student("Yvonne",23,'A')
myobj2.display()
myobj3=Student("Eldad",18,'A')
myobj3.display()
myobj4=Student("Hazel",35,'A')
myobj4.display()
myobj5=Student("Karen",25,'A')
myobj5.display()