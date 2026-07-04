"""
EXCEPTION HANDLING IN PYTHON

What is an Exception?
- An exception is an event that occurs during program execution that disrupts normal flow
- Examples: ZeroDivisionError, ValueError, TypeError, FileNotFoundError, KeyError
- Exceptions allow programs to handle errors gracefully instead of crashing

Why use Exception Handling?
- Prevent program crashes
- Provide meaningful error messages to users
- Allow graceful recovery from errors
- Enable logging and debugging

Syntax:
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Code runs if no exception occurred (optional)
finally:
    # Code that always runs, regardless of exceptions (optional)
"""

# ============================================================================
# 1. BASIC TRY-EXCEPT: Catching a Specific Exception
# ============================================================================
print("--- Example 1: Basic Try-Except ---")
try:
    num = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


# ============================================================================
# 2. MULTIPLE EXCEPTIONS: Handle different error types
# ============================================================================
print("\n--- Example 2: Multiple Exception Types ---")
try:
    user_input = input("Enter a number: ")
    result = 10 / int(user_input)
    print(f"Result: {result}")
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


# ============================================================================
# 3. GENERIC EXCEPTION: Catch any exception (use with caution)
# ============================================================================
print("\n--- Example 3: Generic Exception Handling ---")
try:
    my_list = [1, 2, 3]
    print(my_list[10])  # IndexError
except Exception as e:
    print(f"An error occurred: {e}")
    print(f"Error type: {type(e).__name__}") #returns the name of the exception class as a string.


# ============================================================================
# 4. ELSE CLAUSE: Runs if NO exception occurs
# ============================================================================
print("\n--- Example 4: Try-Except-Else ---")
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful! Result: {result}")


# ============================================================================
# 5. FINALLY CLAUSE: Always executes, used for cleanup
# ============================================================================
print("\n--- Example 5: Try-Except-Finally ---")
try:
    file = open("nonexistent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleanup: This always runs, whether exception occurred or not")


# ============================================================================
# 6. WORKING WITH FILE OPERATIONS
# ============================================================================
print("\n--- Example 6: File Operations with Exception Handling ---")
try:
    with open("example.txt", "w") as f:
        f.write("Hello, World!")
    with open("example.txt", "r") as f:
        print(f"File content: {f.read()}")
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"I/O Error: {e}")
else:
    print("File operations successful!")


# ============================================================================
# 7. DICTIONARY AND LIST OPERATIONS
# ============================================================================
print("\n--- Example 7: Handling KeyError and IndexError ---")
try:
    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["address"])  # KeyError
except KeyError as e:
    print(f"Key not found: {e}")

try:
    my_list = [10, 20, 30]
    print(my_list[5])  # IndexError
except IndexError:
    print("Index out of range!")


# ============================================================================
# 8. RAISING CUSTOM EXCEPTIONS
# ============================================================================
print("\n--- Example 8: Raising Custom Exceptions ---")
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

try:
    validate_age(25)
    print("Age is valid!")
except ValueError as e:
    print(f"Validation error: {e}")


# ============================================================================
# 9. CHAINING EXCEPTIONS: Re-raising with context
# ============================================================================
print("\n--- Example 9: Exception Chaining ---")
try:
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Original error caught: {e}")
        raise TypeError("Cannot perform calculation") from e
except TypeError as e:
    print(f"Final error: {e}")


# ============================================================================
# 10. COMMON EXCEPTIONS IN PYTHON
# ============================================================================
print("\n--- Example 10: Common Built-in Exceptions ---")

exceptions_examples = {
    "ValueError": lambda: int("not_a_number"),
    "TypeError": lambda: "string" + 5,
    "IndexError": lambda: [1, 2, 3][10],
    "KeyError": lambda: {"a": 1}["b"],
    "ZeroDivisionError": lambda: 10 / 0,
    "NameError": lambda: undefined_variable,
    "AttributeError": lambda: "string".nonexistent_method(),
    "FileNotFoundError": lambda: open("missing.txt"),
}

for exc_name, exc_func in list(exceptions_examples.items())[:3]:
    try:
        exc_func()
    except Exception as e:
        print(f"{exc_name}: {e}")


# ============================================================================
# 11. PRACTICAL EXAMPLE: User Input Validation
# ============================================================================
print("\n--- Example 11: Practical User Input Validation ---")
def get_positive_number(prompt="Enter a positive number: "):
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                raise ValueError("Number must be positive!")
            return num
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# Uncomment to test with user input:
# positive_num = get_positive_number()
# print(f"You entered: {positive_num}")


# ============================================================================
# 12. CONTEXT MANAGER: Automatic resource management
# ============================================================================
print("\n--- Example 12: Using Context Manager (with statement) ---")
# The 'with' statement automatically handles opening and closing
try:
    with open("temp.txt", "w") as f:
        f.write("This file will be properly closed automatically")
    print("File written and closed successfully")
except IOError as e:
    print(f"Error: {e}")
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    quotient = numerator / denominator
    print(f"The quotient is: {quotient}")
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Denominator cannot be zero.")