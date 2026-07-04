# Build a Simple Banking System project

'''
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
'''

balance = 1000

def deposit():
    global balance
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Successfully deposited ${amount:.2f}.\nNew balance: ${balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")



def withdraw():
    global balance
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        elif amount <= balance:
            balance -= amount
            print(f"Successfully withdrew ${amount:.2f}.\nNew balance: ${balance:.2f}")
        else:
            print("Insufficient Balance!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def check_balance():
    print(f"Your current balance is: ${balance:.2f}")

def display_menu():
    print("<==========================================================================>")
    print("Welcome to the Banking System")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank you for using the Banking System. Goodbye!")
        break
    else:
        print("Invalid input! Please enter a number between 1 and 4.")





   