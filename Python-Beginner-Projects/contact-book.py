
'''
Contact Book

Features:

Add contact
Delete contact
Search contact
Update phone number

Store contacts in a dictionary.
'''

contact_dict = {}
def display_menu():
    print("<==========================================================================>")
    print("Welcome to the Contact Book")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Update Phone Number")
    print("5. Show Contacts")
    print("6. Exit")



def show_contacts():
    global contact_dict
    if not contact_dict:
        print("No contacts found.")
    else:
        print("Current Contacts:")
        i=0
        for name, number in contact_dict.items():
            i += 1
            print(f"{i}. {name}: {number}")



def add_contact():
    global contact_dict
    name = input("Enter contact name: ")
    contact_number = input("Enter contact number: ")
    contact_dict[name.upper()]=contact_number
    print(f"Contact {name} added successfully!")
   # print("Current Contacts:", contact_dict)

def delete_contact():
    global contact_dict
    name = input("Enter contact name you want to delete: ").upper()
    if name in contact_dict:
        contact_dict.pop(name)
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found!")


def update_phone_number():
    global contact_dict
    name=input("Enter contact name you want to update: ").upper()
    if name not in contact_dict:
        print(f"Contact {name} not found!")
    else:
        new_number=input("Enter new phone number: ")
        contact_dict.update({name: new_number})
        print(f"Contact {name} updated successfully!")


def search_contact():
    global contact_dict
    name = input("Enter contact name you want to search: ").upper()
    if contact_dict.get(name):
        print(f"Contact {name} found: {contact_dict[name]}")
    else:
        print(f"Contact {name} not found!")

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        continue
    if choice == 1:
        add_contact()
    elif choice == 2:
        delete_contact()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_phone_number()
    elif choice == 5:
        show_contacts()
    elif choice == 6:
        print("Thank you for using the Contact Book. Goodbye!")
        break
    else:
        print("Invalid input! Please enter a number between 1 and 6.")



        