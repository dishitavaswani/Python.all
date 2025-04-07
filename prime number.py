#Write a program to check if a number is prime.
n=int(input("Enter Number"))
if(n<=1):
       print(f'{n} is not a prime number.')
else:
    for i in range(2,n):
        if(n%i==0):
            print(f'{n} is not a prime number.')
            break
        else:
            print(f'{n} is a prime number!')
            break
        
