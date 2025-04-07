'''#Write a function to check if a string is a palindrome.
a=str(input('enter a string:'))
if(a==a[::-1]):
    print(f'{a} is a Palindrome')
else:
    print(f'{a} is not a Palindrome')'''


#using fuction
def palindrome(n):
    reversed_a=a[::-1]
    if(a==reversed_a):
        return True
    else:
        return False
a=str(input('enter a string:'))
if(palindrome(a)):
    print(f'{a} is a palindrome')
else:
    print(f'{a} is not a palindrome')
