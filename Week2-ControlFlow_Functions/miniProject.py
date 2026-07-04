# Build a Simple Banking System project

'''
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
'''

balance = 1000
deposit_history = []
withdrawal_history = []
def deposit():
    global balance
    global deposit_history
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            deposit_amount=amount
            deposit_history.append(deposit_amount)
            print(f"Successfully deposited ${amount:.2f}.\nNew balance: ${balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")



def withdraw():
    global balance
    global withdrawal_history
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        elif amount <= balance:
            balance -= amount
            withdrawal_amount=amount
            withdrawal_history.append(withdrawal_amount)
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
    print("4. Transaction History")
    print("5. Exit")


def transaction_history():
    print("Transaction History:")
    if not deposit_history and not withdrawal_history:
        print("No transactions yet.")
        return
    print("Deposits:")
    for deposit in deposit_history:
        print(f"+${deposit:.2f} Deposited")
    print("Withdrawals:")
    for withdrawal in withdrawal_history:
        print(f"-${withdrawal:.2f} Withdrawn")  
        

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 1:
       check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        transaction_history()
    elif choice == 5:
        print("Thank you for using the Banking System. Goodbye!")
        break
    else:
        print("Invalid input! Please enter a number between 1 and 5.")





   