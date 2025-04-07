'''Write a python program to calculate areas of any geometric figures like
circle, rectangle and triangle.'''

'''Area of a circle'''
print('Area of a circle:')
pi = 3.14
r = float(input('enter the radius of a circle:'))
x = pi*r**2
print(f"Area of circle of radius {r} is {x}")
print("\n")

'''Area of rectangle'''
print('Area of rectangle:')
l= float(input('enter the length:'))
w= float(input('enter the width:'))
area = l*w
print(f"Area of rectangle is {area}")
print("\n")

'''Area of Triangle'''
print('Area of triangle:')
b= float(input('enter the base:'))
h= float(input('enter the height:'))
Area = (b*h)/2
print(f"Area of rectangle is {Area}")

         
          
