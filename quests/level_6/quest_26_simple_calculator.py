# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):

    # Prevent division by zero
    if b == 0:
        return "Cannot divide by zero!"

    return a / b

# Ask the user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask the user to choose an operation
operation = input("Choose operation (+, -, *, /): ")

# Call the correct function based on the user's choice
if operation == "+":
    print("Result:", add(num1, num2))
elif operation == "-":
    print("Result:", subtract(num1, num2))
elif operation == "*":
    print("Result:", multiply(num1, num2))
elif operation == "/":
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation!")