'''
Employee Payroll System

Features:

Enter employee details
Calculate salary
Calculate overtime
Print payslip
'''

def input_employee_details():
    employee = {}
    print("--------Employee Payroll System--------")
    employee['name'] = input("Enter employee name: ")
    employee['id'] = input("Enter employee ID: ")
    employee['designation'] = input("Enter employee designation: ")
    employee['basic_salary'] = float(input("Enter basic salary: "))
    employee['overtime_hours'] = float(input("Enter overtime hours: "))
    return employee


def calculate_salary(employee):
    basic_salary = employee['basic_salary']
    overtime_hours = employee['overtime_hours']
    overtime_rate = 20  # Assuming $20 per hour for overtime
    overtime_pay = overtime_hours * overtime_rate
    total_salary = basic_salary + overtime_pay
    return total_salary

def print_payslip(employee, total_salary):
    print("\n--- Payslip ---")
    print(f"Employee Name: {employee['name']}")
    print(f"Employee ID: {employee['id']}")
    print(f"Designation: {employee['designation']}")
    print(f"Basic Salary: ${employee['basic_salary']:.2f}")
    print(f"Overtime Hours: {employee['overtime_hours']}")
    print(f"Total Salary: ${total_salary:.2f}")
    print("----------------\n")


def main():
    employee = input_employee_details()
    total_salary = calculate_salary(employee)
    print_payslip(employee, total_salary)   


if __name__ == "__main__":
    main()

