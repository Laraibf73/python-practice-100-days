'''
POLYMORPHISM : many forms

complex numbers: hv imaginary & real part
Operation Overloading: when the same operator is allowd to have a diff. meaning according to the context.
'''

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def display_Number(self):
        print(f'{self.real}i + {self.img}j')

#Dunder func any function having __ in prefix or postfix
    def __add__(self,num2): # (obj1 & obj2)
        newReal=self.real+num2.real
        newImg=self.img + num2.img
        return Complex(newReal , newImg)


    def __sub__(self,num2): # (obj1 & obj2)
        newReal=self.real-num2.real
        newImg=self.img - num2.img
        return Complex(newReal , newImg)


num1=Complex(2,1)
num1.display_Number()

num2=Complex(4,3)
num2.display_Number()

num3=num1 + num2
num3.display_Number()

num4 = num1 - num2
num4.display_Number()




# Define a Circle class with radius as a constructor. Find area & perimeter of a circle

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def Area(self):
        return (2*3.14*self.radius**2)

    def perimeter(self):
        return (2*22/7*self.radius)
c1=Circle(21)
print(c1.Area())
print(c1.perimeter())


# Define Employee class with attributes role,department & salary. Show these details in a method.
# Create another class Engineer inherited from Employee class with two more attributes name & age.
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    
    def show_Details(self):
        print(f'Empolyee Role: {self.role}')
        print(f'Empolyee Department: {self.dept}')
        print(f'Empolyee Salary: {self.salary}')

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Developer","Software",1000)




e=Engineer("Ayesha",24)
e.show_Details()



# Create a class Order which stores items & its prices
# use a dunder func __gt__ {greater} order1 price is greater than order2 returns in a form of true or false.

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,o2):
        return (self.price > o2.price)


o1=Order('Chips',50)
o2=Order('Tea',30)


print(o1>o2)
