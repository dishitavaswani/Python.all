'''#Write a program to find the largest of three numbers.
a=float(input('Enter 1st Number:'))
b=float(input('Enter 2st Number:'))
c=float(input('Enter 3st Number:'))
if(a<=b<c):
    print(f'largest number is {c}')
elif(a<=c<b):
    print(f'largest number is {b}')
elif(c<=b<a):
    print(f'largest number is {a}')
else:
    print(f'{a}={b}={c}')'''

#using function
def MAX(a,b,c):
    if a<=b<=c:
        return c
    elif b<=c<=a:
        return a
    else:
        return b
    
x=int(input('enter 1st number:'))
y=int(input('enter 2st number:'))
z=int(input('enter 3st number:'))
largest=MAX(x,y,z)
print(f'The largest of the 3 numbers is {largest}')



    
        


    

