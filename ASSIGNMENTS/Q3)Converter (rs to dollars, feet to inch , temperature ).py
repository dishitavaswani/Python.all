'''Develop any converter such as Rupees to dollar, temperature converter,
inch to feet etc.'''

'''Rupees to Dollar'''
print("Rupees to Dollars")
r= float(input("Enter the amount in Rupees:"))
d = r/84
print(f"{r} rs in dollars is {d:0.2f}")
print('\n')

'''Temperature Converter'''
print("Celsius to Farenhiet")
c = float(input("Enter the temperature in Celsius:"))
f = (9*c)/5 + 32
print(f"{c} degree celsius to farenhient is {f}")
print("\n")

'''inch to feet'''
print("Inches to feets")
inch = float(input("Enter the height in inches:"))
feet = inch/12
print(f"{inch} inches is {feet} feet.")

