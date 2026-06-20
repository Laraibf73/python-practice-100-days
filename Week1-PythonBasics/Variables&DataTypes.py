
'''
What is Python?

- Python is simple & easy

- Free & Open Source

- High Level Language

- Developed by Guido van Rossum

- Portable

'''


#Simple Print statement

print('Hello World!')


#Variables & Data Types

a=9
b="Harray"
c=9.0
d=True
e=complex(9,3)
f=None
g='V'

print(a,"\n",b,"\n",c,"\n",d,"\n",e)

name='Lara'
age=20
price=9.45
name1='Ayesha'
age1=age

print("My name is ",name)
print("Age of ",name1," is same of ",name," i.e",age1)

print('<====== DATA TYPES =====>')

print(type(a))  # int
print(type(b)) # str
print(type(c)) # float
print(type(d)) # bool
print(type(e)) # complex
print(type(f)) # NoneType


# Arithematic Operators

print('<====== Arithmetic Operators ======>')

a=5
b=2  

print(a+b) 
print(a-b) 
print(a*b) 
print(a/b)  
print(a**b) #a^b
print(a%b) #remainder


#Relational Operators
print('<====== Relational Operators ======>')

a=50 
b= 20 

print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a<=b) # False


#Assignment Operators
print('<====== Assignment Operators ======>')
num =10
num+=10
print("Num is :",num)

num2=10
num2 **=5
print("Num power :",num2) # 1,00,000



#Logical Operators
print('<====== Logical Operators ======>')

val1=True
val2=False

print("AND  operator ", val1 and val2)
print("OR  operator", val1 or val2)

a=50 
b=20 

print("NOT operator",not(a<b))
print("OR operator on exp ", (a==b) or (a>b))


#Input from user

name = input("Enter ur name: ")
print("Welcome ",name)


number = input("Enter any number: ")
print(type(number),number) #"45" , "66.54"

n = int(input("Enter any number: "))
print(type(n),n)


name = input("Enter Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

print("Name = ",name)
print("Age = ",age)
print("Marks = ",marks)



#Let‘s Practice

# Write a Program to input 2 numbers & print their sum.

n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))

print("Sum of ",n1," & ",n2," = ", n1+n2)


# WAP to input side of a square & print its area.

length = float(input("Enter side of a square: "))
print("Area of square is = ", length**2)


# WAP to input 2 floating point numbers & print their average.

n1=float(input("Enter n1: "))
n2=float(input("Enter n2: "))

print("Average of ",n1," & ",n2," = ", (n1+n2)/2) 

# WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False.
a=int(input("Enter a: "))
b=int(input("Enter b: "))

print("a >= b ",a>=b)