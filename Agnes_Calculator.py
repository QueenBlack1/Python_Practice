def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2): 
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 / num2

# Get user input and convert to floats
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

operator = input('Enter an operator (+, -, *, /): ')

# Perform operation based on operator
if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operator."

print("Result:", result)