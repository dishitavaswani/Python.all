'''Using function, write a Python program to analyze the input number is
prime or not.'''

def prime_number(n):
    if n<= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True

x = int(input("Enter a number: "))

if prime_number(x):
    print(f"{x} is a prime number!")
else:
    print(f"{x} is not a prime number.")

