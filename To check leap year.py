#Write a program to check if a year is a leap year.
n=int(input('Enter Year:'))
if(n%4==0 and n%100!=0):
   print(f'{n} is a leap year!')
else:
   print(f'{n} is not leap year!')
