class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"


# Creating an object of class Dog
my_dog = Dog("Buddy", 5)

# Accessing attributes and methods
print(my_dog.name)  # Outputs: Buddy
print(my_dog.bark())  # Outputs: Buddy says Woof!
