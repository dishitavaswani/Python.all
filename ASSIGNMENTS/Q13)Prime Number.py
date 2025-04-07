'''Using function, write a Python program to analyze the input number is
prime or not.'''

def primenumber(n):
    if n < 0:
        return None
    elif n == 1 or n == 0:
        return None
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
            else:
                return True
x = int(input("Enter a number:"))
if primenumber(x):
    print(f"{x} is a prime number")
elif primenumber(x) is None:
    print("It is either invalid input ot the number is neither prime nor composite")
else:
    print(f"{x} is not a prime number")

