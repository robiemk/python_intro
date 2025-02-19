class Cars:
    #constructor method
    def __init__(self, make, model, color, yom):
        self.make = make
        self.model = model
        self.color = color
        self.yom = yom
        #Member Function
    def display(self):
        print(f"The make is the {self.make} and model{self.model} color is {self.color} finally yom being {self.yom}")
myobj=Cars("Toyota","MK4 Supra","Blue",1996)
myobj.display()
myobj2=Cars("Nissan","Skyline","White",1998)
myobj2.display()
myobj3=Cars("Toyota/Lexus","LFA","Silver Metallic",2010)
myobj3.display()
myobj4=Cars("Mazda","RX7","Sunrise Red",1997)
myobj4.display()
myobj5=Cars("Subaru","WRX STI","WR Blue Pearl",2004)
myobj5.display()
