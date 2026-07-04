# LOOPS

count=1
while count<=5:
    print("Hello")
    count+=1

i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue # skip
    print(i)
    i+=1


print("<==== Let‘s Practice ====>")

# Print numbers from 1 to 100.
num=1
while num<=100:
    print(num)
    num+=1

#Print numbers from 100 to 1.
num=100
while num>=1:
    print(num)
    num-=1


# Print the multiplication table of a number n.

n=int(input("Enter a number"))
i=1
while i<=10:
    print(n,' * ',i,'= ',n*i)
    i+=1 

# Print the elements of the following list using a loop:
list= [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i=0
while (i<len(list)):
    print(list[i])
    i+=1


# Search for a number x in this tuple using loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

x=int(input("Enter a number to be searched "))
tuple= (1, 4, 9, 16, 25, 36, 49, 64, 81,100,36)
i=0
while (i<len(tuple)):
    if(tuple[i]==x):
        print("Number you are searching for is present in the list on index",i)
    i+=1
          

       
# FOR LOOP

tup=(9,5,4,3,2,1,6)
for i in tup:
    print(i)

# Print the elements of the following list using a loop:

list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for el in list:
    print(el)



# Search for a number x in this tuple using loop:
lis = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x=int(input('Enter a num: '))
idx=0
for i in lis:
    if(i==x):
        print('Number found at index: ',idx)
    idx+=1



# range( )

# range( start?, stop, step?)
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by
# 1 (by default), and stops before a specified number.

# range( start?, stop, step?)

for el in range(5): #range(stop)
    print(el)



for el in range(3,5): #range(start,stop)
    print(el)

for el in range(0,10,2): #range(start,stop)
    print(el)


 #   Let‘s Practice

# Print numbers from 1 to 100.
#for el in range(1,101):
 #   print(el)

# Print numbers from 100 to 1.

#for el in range(100,0,-1):
   # print(el)

# Print the multiplication table of a number n.

n=2
for el in range(1,11):
    print(el*n)


   # WAP to find the sum of first n numbers. (using while)

n=5
sum=0
for i in range(1,n+1):
    sum+=i
print('sum is ',sum)


n=5
sum=0
i=0
while i <= n:
    sum+=i
    i+=1
print('sum is ',sum) 

# WAP to find the factorial of first n numbers. (using for)

n=5
fac=1
for i in range(1,n+1):
    fac *=i
print('factorial = ',fac) # 120