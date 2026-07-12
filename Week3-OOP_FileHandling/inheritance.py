'''
Inheritance is a way of creating a new class for using details of an existing class without modifying it.
 The newly formed class is a derived class (or child class).
 The existing class is a base class (or parent class).

'''
'''
class Car():
    @staticmethod
    def Start():
        print("Car is starting")

    @staticmethod
    def Stop():
        print("Car is stopping")

class Toyota(Car):
    def __init__(self,name):
        self.name=name

c1=Toyota("Camry")
c2=Toyota("Fortuner")

print(c2.Start())
print(c2.name)
print(c2.Stop())
'''

#super() function is used to give access to the methods of a parent class from a child class. 

class Car():

    def __init__(self,typ):
        self.type=typ


    @staticmethod
    def Start():
        print("Car is starting")

    @staticmethod
    def Stop():
        print("Car is stopping")

class Toyota(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().Start()
        super().Stop()


c=Toyota('Prius','electric')
print(c.name)
print(c.type)




#decorator: @classmeethod()
class Person:
    name="Anonymous"

    def changeName(self,name):
        self.name=name

    @classmethod
    def modifyName(cls,name):
        cls.nm=name

s=Person()
s.changeName("Ahmed Faraz")
print(s.name) # Ahmed Faraz
print(Person.name) # Anonymous


s.modifyName("Ayesha Khan")
print(s.nm) # Ayesha Khan
print(Person.nm) # Ayesha Khan


