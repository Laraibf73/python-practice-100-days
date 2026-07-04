'''
Student Grade Management System

Features:
    Add student
    Add marks
    Calculate average
    Find topper
    Display grades

Concepts:
    Lists
    Dictionaries
    Functions
'''

student_dict = {}
marks_list=[]

def display_menu():
    print("<==========================================================================>")
    print("Welcome to the Student Grade Management System")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. Calculate Average")
    print("4. Find Topper")
    print("5. Display Grades")
    print("6. Exit")

def add_student():
    global student_dict
    name = input("Enter student name: ")
    student_dict[name.upper()] = marks_list
    print(f"Student {name} added successfully!")


def add_marks():
    global student_dict
    name = input("Enter student name: ")
    if name.upper() in student_dict:
        marks = input("Enter marks (comma-separated): ")
        marks_list = [int(mark) for mark in marks.split(",")]
        student_dict[name.upper()] = marks_list
        print(f"Marks for {name} added successfully!")
    else:
        print(f"Student {name} not found. Please add the student first.")


def display_grades():
    global student_dict
    if not student_dict:
        print("No students found.")
        return
    for name, marks in student_dict.items():
        print(f"Student: {name}, Marks: {marks}")

def calculate_average():
    global student_dict
    global marks_list
    name = input("Enter student name: ")
    if name.upper() in student_dict:
        marks_list = student_dict[name.upper()] #extracting marks list for the student
        print(marks_list)
        if marks_list:
            average = sum(marks_list) / len(marks_list)
            print(f"Average marks for {name}: {average:.2f}")
        else:
            print(f"No marks found for {name}.")




def find_topper():
    global student_dict
    if not student_dict:
        print("No students found.")
        return
    topper = None
    highest_average = 0
    for name, marks in student_dict.items():
        if marks:  # Check if the student has marks
            average = sum(marks) / len(marks)
            if average > highest_average:
                highest_average = average
                topper = name
    if topper:
        print(f"The topper is {topper} with an average of {highest_average:.2f}")
    else:
        print("No marks found for any student.")

while True:
    display_menu()
    try:
        choice=int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        continue    
    if choice == 1:
        add_student()
    elif choice == 2:
        add_marks()
    elif choice == 3:
        calculate_average()
    elif choice == 4:
        find_topper()
    elif choice == 5:
        display_grades()
    elif choice == 6:
        print("Thank you for using the Student Grade Management System. Goodbye!")
        break