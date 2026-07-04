print("<==== L I S T S ====>")
#It is a built-in data type that stores set of values (int,float,str)
# Lists are mutable while strings were not.
# stores data of multiple data types.

list=["Ali",20,"Islamabad","Ahmad",18,"Karachi"]

print(type(list))
print(len(list))
print(list[3])
list[1]=10
print(list)


# List Slicing

marks=[2.1,45.0,67.5,88.0,33.0]
print(marks[1:4]) #[45.0,67.5,88.0]
print(marks[:3]) # [2.1,45.0,67.5]
print(marks[-3:-1]) # [67.5,88.0]


# List Methods
'''
list.append(4) #adds one element at the end
list.insert( idx, el ) #insert element at index
list.sort( ) #sorts in ascending order
list.reverse( ) #reverses list
list.sort( reverse=True ) #sorts in descending order
'''

list=[3,1,2]
print(list.append(4)) # None
list.insert(3,5)
print(list.sort()) # None
print(list)
print(list.sort(reverse=True))
print(list)



list_str=["banana","plum","apple","apricot"]

print(list_str.sort()) # None
print(list_str)
list_str.reverse() 
print(list_str)


l=[0,3,1,2,1]
l.remove(1) #removes first occurrence of element
print(l)
l.pop(1) # removes element at index
print(l)


print("<==== T U P L E S ====>")
# A built-in data type that lets us create immutable sequences of values.

tup=(92,1,3,1)
tuple=()
tuple=(1) # python will treat it as a normal int val
print(type(tuple))
tuple=(1,)
print(type(tuple))


tup = (2, 1, 3,4,1, 1)

# tup.count( el ) counts total occurrences tup.count(1) is 2
print(tup.count(1)) # 3
print(tup.index(2)) #  0 returns index of first occurrence

print("<==== Let‘s Practice ====>")

# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
'''
list=[]

list.append(input("Enter first movie name: "))
list.append(input("Enter second movie name: "))
list.append(input("Enter third movie name: "))
print(list)'''

# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1] [1,“abc”,“abc”, 1]

a=[1,'abc','abc', 1]
b=a.copy()
a.reverse()
if(a==b):
    print("list is a palindrome")
else:
    print("list is not a palindrome")

# WAP to count the number of students with the “A” grade in the following tuple.
# (”C”,“D”,“A”,“A”,“B”,“B”,“A”)

grade=('C','D','A','A','B','B','A')

print(grade.count('A')) # 3

# Store the above values in a list & sort them from “A” to “D”
lis=['C','D','A','A','B','B','A']
lis.sort()
print(lis)