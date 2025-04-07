'''Write a Python program to print a triangle pattern (give any),
emphasizing the transition from C to Python syntax.'''

x = int(input("Enter the number of rows:"))


print("Increasing Half Triangle:")
for i in range(x+1):
    for j in range(i+1):
        print("*",end=" ")
    print()

print("Decreasing Half Triangle:")
for i in range(x):
    for j in range(x-i):
        print("*",end=" ")
    print()

print("Right side Increasing Triangle")
for i in range(x+1):
    for j in range(x-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
print()

print("Right side decreasing Triangle")
for i in range(x):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(x-i):
        print("*",end=" ")
    print()
print()

print("Triangle")
for i in range(x+1):
    for j in range(x-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
print()

print("Upside Down Triangle")
for i in range(x+1):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(2*(x-i)-1):
        print("*",end=" ")
    print()
print()

print("Diamond")
for i in range(x):
    for j in range(x-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(x):
    for j in range(i):
        print(" ",end=" ")
    for k in range(2*(x-i)-1):
        print("*",end=" ")
    print()
print()


print("Diamond with space")
for i in range(x):
    for j in range(x-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
print()
for i in range(x):
    for j in range(i):
        print(" ",end=" ")
    for k in range(2*(x-i)-1):
        print("*",end=" ")
    print()
print()



    
    
