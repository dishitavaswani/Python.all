#Write a function to calculate the sum of all numbers in a list.
def SUM(n):
    return sum(n)
a=list(map(int,input('enter the numbers: ').split()))
print(f'the sum of all elements in list {a} is {SUM(a)}')

#without lists

b=list(map(int,input('enter the list: ').split()))
total_sum=sum(b)
print(f'The sum of all elements in list {b} is {total_sum}')


