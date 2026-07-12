'''
Class: Blueprint of an object. It defines the properties and behaviors that the object will have. 
In Python, classes are defined using the 'class' keyword, followed by the class name and a colon.
 Inside the class, we can define attributes (variables) and methods (functions) that belong to the class.

 Object: An instance of a class. It is created from the class blueprint and has its own unique state and behavior.

 constructor: A special method in a class that is called when an object is created. 
 In Python, the constructor is defined using the '__init__' method. It is used to initialize the attributes of the object.
'''


#Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

#static method used to define a method that belongs to the class rather than an instance of the class.
    @staticmethod
    def collegeName():
        print("ABC College")

    def average(self):
        sum=0
        for mark in self.marks:
            sum+=mark
        return sum/len(self.marks)


s1=Student("John",[80,90,70])
s1.collegeName()
print('Average marks for', s1.name, ':', s1.average())




#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self,accountno,balance):
        self.accountno=accountno
        self.balance=balance

    def debit(self,amount):
        if amount>self.balance:
            print("Insufficient Balance!")
        else:
            self.balance-=amount
            print("Debited:", amount)
            print("Total Balance ",self.displayBalance())


    def credit(self,amount):
        self.balance+=amount
        print("Credited:", amount)
        print("Total Balance ",self.displayBalance())


    def displayBalance(self):
        return self.balance

a=Account("123456",1000)
a.debit(500)
a.credit(200)
a.credit(2000)



#delete an attribute from an object using the 'del' keyword.
class Student:
    def __init__ (self,name):
        self.name=name
    

s1=Student("John")
'''del s1
print(s1.name)  # This will raise a NameError since the object 's1' has been deleted.
del s1.name
print(s1.name)  # This will raise an AttributeError since the 'name' attribute has been deleted.
'''


#private attributes and methods in Python are defined by prefixing the attribute or method name with double underscores (__).

class Account:
    def __init__(self,secret_pin,accno):
        self.__secret_pin=secret_pin  # private attribute
        self.accno=accno  # public attribute

    def reset_pin(self):
        print("password is",self.__secret_pin)  # private method

a=Account("1234","123456")
print(a.accno)
a.reset_pin()  # This will work since the 'reset_pin' method is public and can access the private attribute '__secret_pin'.
print(a.__secret_pin)  # This will raise an AttributeError since the '__secret_pin' attribute is private.