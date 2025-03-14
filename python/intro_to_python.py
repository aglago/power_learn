# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation_string = """Enter:
1 for Addition(+)
2 for Subtraction(-)
3 for Multiplication(X)
4 for Division(/)
"""
operation = int(input(operation_string))

if operation == 1:
    print(num1, "+", num2, "=", num1 + num2)
elif operation == 2:
    print(num1, "-", num2, "=", num1 - num2)
elif operation == 3:
    print(num1, "X", num2, "=", num1 * num2)
elif operation == 4:
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Enter the right operation")
