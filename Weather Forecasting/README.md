<h1><b>Simple Calculator Project Overview </b></h1


Aim:
Create a user-friendly console-based calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

Objectives:

Accept two numeric inputs and an operation choice from the user.

Perform the requested arithmetic operation.

Handle errors such as invalid input and division by zero.

Allow continuous calculations until the user decides to exit.

Features:

Text-based user interface via console.

Functions for each arithmetic operation.

Input validation and error handling using try-except blocks.

Loop to enable multiple calculations without restarting.

Sample Python Code for a Basic Calculator
python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

        next_calc = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calc != 'yes':
            print("Thank you for using the calculator.")
            break

if __name__ == "__main__":
    calculator()
Explanation
The program defines functions for each operation.

It uses a loop to continuously prompt the user for an operation and two numbers.

Input validation ensures only valid choices and numeric inputs are accepted.

Division by zero is specifically handled with an error message.

The user can perform multiple calculations until they choose to exit.

This project is ideal for beginners to understand basic programming concepts like functions, loops, conditionals, and error handling in a practical context
