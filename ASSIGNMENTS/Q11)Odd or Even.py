'''Develop a Python program that takes a numerical input and identifies
whether it is even or odd, utilizing conditional statements and loops.'''


while True:
    x = int(input("Enter any number:"))
    if(x < 0 and x == 0):
        print("Invalid Input!")
        continue
    if x%2 == 0:
        print(f"The number {x} is even")
    else:
        print(f"The number {x} is odd")
    break

x= int(input("Enter any number:"))
while(x != 0 and x > 0):
    if x%2 == 0:
        print(f"The number {x} is even")
    else:
        print(f"The number {x} is odd")
    break
