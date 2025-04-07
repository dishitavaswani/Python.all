'''Design a Python program to compute the factorial of a given integer N.'''
def fact(n):
    if (n==1 or n ==0):
        return 1
    elif(n<0):
        print("Invalid Input")
    else:
        return n*fact(n-1)

a = int(input("Enter any number:"))
x = fact(a)
print(f"Factorial of {a} is {x}")
