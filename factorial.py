#Write a function to calculate the factorial of a number.

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
         return n*factorial(n-1)
        
a=int(input('Enter Number:'))
print(factorial(a))
      
