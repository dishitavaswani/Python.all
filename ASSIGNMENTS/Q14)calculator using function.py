'''Implement a simple Python calculator that takes user input and performs
basic arithmetic operations (addition, subtraction, multiplication,
division) using functions.'''
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
         print("Error! Division by Zero gives Infinity")

num1 = float(input("Enter the 1st Number:"))
num2 = float(input("Enter the 2st Number:"))

print(f"The result of Addition is {add(num1, num2)}")
print(f"The result of Subtraction is {sub(num1, num2)}")
print(f"The result of Multiplication is {multiply(num1, num2)}")
print(f"The result of Division is {divide(num1, num2)}")

    
        
