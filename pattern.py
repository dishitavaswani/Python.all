#Pattern
n=int(input("enter the number of rows"))

#increasing half triangle
print('increasing half triangle')
for i in range(n+1):
    for j in range(i+1):
        print("*",end="")
    print()
#decreasing half triangle
print('decreasing half triangle')
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()

#right sided triangle increaing
print('right sided triangle increaing')
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    print(' ')
print()

#right sided triangle decreasing
print('right sided triangle decreasing')
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
        print('*',end=' ')
    print(' ')
print()

#Half diamond 
print('half diamond')
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(2*i-1):
        print('*',end=' ')
    print()
print()

#half triangle reverse
print('half triangle reverse')
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print('*',end=' ')
    print()
print()

#Diamond Pattern
print('diamond')
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(2*i-1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print('*',end=' ')
    print()
print()

#Diamond Pattern space in between
print('diamond with space')
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(2*i-1):
        print('*',end=' ')
    print()
print()
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print('*',end=' ')
    print()
print()



