print("<==== RECURSION ====>")

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

print(factorial(5))'''


'''
Let‘s Practice

Write a recursive function to calculate the sum of first n natural numbers.

Write a recursive function to print all elements in a list.
Hint : use list & index as parameters.'''


# Write a recursive function to calculate the sum of first n natural numbers.
'''
def sum(n):
    s=0
    if(n==0):
        return 0
    return sum(n-1)+n

print(sum(5))'''

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def print_lis(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_lis(list,idx+1)

l=["apple","mango","banana"]
print_lis(l)