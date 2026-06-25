# Day 5: Practice Exercises



# Print your name, age, and city.
print("Name: Laraib")
print("Age: 23")
print("City: Islamabad")


# Take two numbers from the user and print their sum, difference, multiplication, and division.

a=int(input("Enter a first number "))
b=int(input("Enter a second number "))
print("Sum of",a," $ ",b," :", a+b)
print("Difference",a," $ ",b," :", a-b)
print("Product of",a," $ ",b," :", a*b)
print("Division of",a," $ ",b," :", a/b)


# Convert temperature from Celsius to Fahrenheit. (0°C × 9/5) + 32 = 32°F)

temp=float(input("Enter temperature in Celsius "))
temperature=(temp*(9/5))+32
print("Temperature in F is ",temperature,'F')


# Calculate the area of a rectangle.
l=int(input("Enter a length "))
b=int(input("Enter a width "))
print("Area of rectangle = ",l*b)



# Check whether a number is even or odd.
num=int(input("Enter a number "))
if num%2==0:
    print("Number is Even")
else :
    print("Number is Odd")


# Find the largest of three numbers.
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
if(a>b and a>c):
    print(a," is largest of all")
elif(b>a and b>c):
    print(b," is largest of all")
else:
    print(c," is largest of all")




# Calculate the average of five numbers.
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
d=int(input("Enter fourth number "))
e=int(input("Enter fifth number "))
print("Average of 5 numbers = ", (a+b+c+d+e)/5)


# Swap two variables without using a third variable.
a=5
b=10
a,b=b,a
print(a)
print(b)

# Convert minutes into hours and minutes.
mins =130
hours=130/60
minutes=130%60
print("Hours & minutes =",int(hours)," & ",int(minutes)," mins")


# Calculate simple interest.
principal=40
interestRt=10
timesInYrs=3
print("Interest is ",principal*interestRt*timesInYrs)



print("<==== String Exercises ====>")


# Count the number of characters in a string
str="Count the number of characters in a string"
print(len(str))

# Reverse a string
str="HELLO"
print(str[::-1])


# Check if a string is a palindrome
str="abcba"
print(str[::-1])


# Count vowels in a string
str="Hello World vOwels"
count=0
for el in str.lower():
    if(el =='a' or el=='e' or el=='i' or el=='o' or el=='u'):
        count+=1
print(count)

# Convert a string to uppercase and lowercase.
str1="hello"
str2='WORLD'

print(str1.upper())
print(str2.lower())



print("<==== List Exercises ====>")

'''Find the largest element in a list.
Find the smallest element in a list.
Calculate the sum of all elements.
Remove duplicates from a list.
Sort a list without using sort().'''

# Find the largest element in a list
list=[87, 64, 33, 95, 76]

print("Largest ",max(list))

# Find the smallest element in a list
list=[87, 64, 33, 95, 76]
print("Smallest ",min(list))


# Calculate the sum of all elements

list=[87, 64, 33, 95, 76]

sum=0
i=0
while i<len(list):
    sum+=list[i]
    i+=1
print("Sum =", sum)


# Remove duplicates from a list.
list = [{"id": 1}, {"id": 2}, {"id": 1}]

new_list=[]

for items in list:
    if items not in new_list:
        new_list.append(items)
print(new_list)
