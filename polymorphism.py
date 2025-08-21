
import inheritance
class car:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def move(self):
        print("Drive! its a car")

class boat:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def move(self):
        print(f"sail ! is a {self.model}")

class plane:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def move(self):
        print(f"fly ! is a {self.model}")

car1=car("Tesla","modal x")
boat1=boat("cyber","modal y")
plane1=plane("147","modal,z")

for x in (car1,boat1,plane1):
    x.move()


a = inheritance.person1["age"]
print(a)


inheritance.s1.studentintroduce()