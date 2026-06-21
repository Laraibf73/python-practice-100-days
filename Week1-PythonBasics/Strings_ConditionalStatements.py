# S T R I N G S
# It is a data type that stores sequence of characters.
print('\n\n <==== STINGS ====>')


str1="This is a String"
str2='This is a String'
str3="""This is a String"""
str4="This is Sara's umbrella"

#Escape Sequence
str="This is a String.\nWe are using it in a Python." #NextLine
print(str)

str="This is a String.\tWe are using it in a Python." #tab
print(str)

print('\n\n <==== Concatenation ====>')

# Concatenation => Joining 2 strings
s1='Hello'
s2='World!'
concat=s1+s2
print(concat)

concat=s1+' '+s2
print('Length of s1: ',len(s1))
print('Length of s2: ',len(s2))
print('Length of concatenated string: ',len(concat))


# Length
s='Institution'
print(len(s))

# Indexing => helps to access chars from any position but we can't mutate them

string="PYTHON_BASICS"
print(string[6]) # _

# string[0]="&" # X gives error
print('\n\n <==== Slicing ====>')


# Slicing
# slice[starting_idx:ending_idx] -> ending_idx is not included. 
# 0 1 2 3 4 5 6 7 8 9 10 11 12
# P Y T H O N _ B A S  I  C  S

string="PYTHON_BASICS"
print(string[3:8]) #HON_B
print(string[5:10]) #N_BAS

print( string[:6]) # str[0:6]
print( string[4:]) # str[0:len(string)]

# Negative Slicing
# A P P L E
# -5-4-3-2-1
str="APPLE"
print(str[-3:-1]) #PL


str="i am learning Python from Youtube."
print(str.endswith('ube.')) # true # returns true if string ends with substr
print(str.endswith('ubE.')) # False
print(str.endswith('age.')) # False

print(str)
print(str.capitalize()) # #capitalizes 1st char
str=str.capitalize()
print(str)


print(str.replace("python", 'Java')) #replaces all occurrences of old with new
print(str.replace("o", 'u'))

# str.find( word ) returns 1st index of 1st occurrence
print(str.find('i'))
print(str.find('python'))
print(str.find('Python'))

# str.count(“am“) counts the occurrence of substr in string
print(str.count('o'))


print('\n\n <==== Let‘s Practice ====>')


# Let‘s Practice

# WAP to input user’s first name & print its length.
name=input('Enter ur Name: ')
print('Length of ur first name is: ',len(name))

# WAP to find the occurrence of ‘$’ in a String.
str="1 PKR $is equal to $400"
print(str.count('$'))


#Conditional Statement
print('\n\n <==== CONDITIONAL STATEMENT ====>')
Age=18
if(Age>=18): print("Can Vote")
else:print("Cannot Vote")


marks=int(input('Enter ur makrs: '))
if(marks>=90):
    grade='A'
elif(marks<90 and marks>=80 ):
     grade ='B'

elif(marks<80 and marks>=70 ):
    grade='C'
elif(marks<70):
    grade='D'
else:
    grade='F'

print("Your grade is ",grade)


print('\n\n <==== Let‘s Practice ====>')

# Let‘s Practice

# WAP to check if a number entered by the user is odd or even.

num=int(input('Enter a number: '))
if(num%2==0):
    print(num," is Even.")
else:
    print(num," is Odd.")

# WAP to find the greatest of 3 numbers entered by the user.

n1=int(input('Enter a number: '))
n2=int(input('Enter a number: '))
n3=int(input('Enter a number: '))

if(n1>=n2 and n1>=n3):
    print(n1," is greatest of all.")
elif(n2>=n1 and n2>=n3):
        print(n2," is greatest of all.")
else:
    print(n3," is greatest of all.")

# WAP to check if a number is a multiple of 7 or not.
num=int(input('Enter a number: '))
if(num%7==0):
    print(num," is a multiple of 7.")
else:
    print(num," is not a multiple of 7.")