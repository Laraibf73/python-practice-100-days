print("<==== FUNCTIONS ====>")

#function definition
def cal_sum(a,b): # paramenters
    return(a+b)

sum =cal_sum(9,12) # function call & arguments
print(sum)

print(cal_sum(2,3))


def print_hello():
    print("Hello")

output=print_hello()
print(output) #None


def average(a,b,c):
    sum=a+b+c
    avg=sum/3
    print("Average = ",avg)
    return avg

average(2,1,3)

# def calc_product(b,a=2): default values are assigned from the end

def calc_product(a=2,b=3):
    print(a*b)
    return a*b

calc_product() #default params


'''
Let‘s Practice

WAF to print the elements of a list in a single line. ( list is the parameter)

WAF to find the factorial of n. (n is the parameter)
WAF to print the length of a list. ( list is the parameter)

WAF to convert USD to INR.'''

# WAF to print the elements of a list in a single line. ( list is the parameter)

def print_el(list=[2,6,7,8,4,4]):
    for el in list:
        print(el,end=" ")
    return el

print_el() 

# WAF to find the factorial of n. (n is the parameter)

def calc_Fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print("Factorial of ",n," = ",fact)
    return fact

calc_Fact(5) 


# WAF to print the length of a list. ( list is the parameter)

def list_len(l):
    print("Length of a list = ",len(l))
    return len(l)

list_len([3,5,6,7,9,34,2,4,7,"hat",'&']) 


# WAF to convert USD to PKR.
# 1$=278.16 PKR

def ccyConvrter(ccy):
    PKR=ccy*278.16
    print("$",ccy,"=",PKR,"PKR")
    return PKR

ccyConvrter(9) 


# Input Number from a user and return wether its even or odd.

num=int(input("Enter a num "))

def evenOdd(n):
    if(num%2==0):
        str="EVEN"
    else:
        str="ODD"
    print(str)
    return str

evenOdd(num)