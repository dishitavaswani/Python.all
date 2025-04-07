'''Write a Python program to explore basic arithmetic operations. The
program should prompt the user to enter two numbers and then perform
addition, subtraction, multiplication, division, and modulus operations on
those numbers. The results of each operation should be displayed to the
user.'''

a = int(input("Enter 1st Number:"))
b = int(input("Enter 2st Number:"))
b != 0
print("Addition:")
x = a + b
print(f"Addition of {a} and {b} is {x}")
print("\n")
print("Subtraction:")
y = a - b
print(f"Subtraction of {a} and {b} is {y}")
print("\n")
print("Multiplication:")
z = a*b
print(f"Multiplication of {a} and {b} is {z}")
print("\n")
print("Division:")
d = a/b
print(f"Division of {a} and {b} is {d}")
print("\n")
print("Modulus:")
m = a % b
print(f"Modulus of {a} and {b} is {m}")
print("\n")
print("2nd num in power of 1st num:")
p = a ** b
print(f"2nd num in power of 1st num is {p}")
print("\n")

