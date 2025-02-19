class Dad:
    def __init__(self,color,dadhobby):
        self.color=color
        self.dadhobby=dadhobby
class Mum:
    def __init__(self,color,mumhobby):
        self.color=color
        self.mumhobby=mumhobby
class Boy(Dad,Mum):
    def boyinherits(self):
        print(f"Boy inherits {self.color} and {self.dadhobby}")

#instance
myobj=Boy("African Descent","Watching Formula one")
myobj.boyinherits()

class Girl(Mum):
    def girlinherits(self):
        print(f"Girl inherits {self.color} and {self.mumhobby}")
myobj2=Girl("light skin-tone","Shopping")
myobj2.girlinherits()

