'''Write a Python program to calculate the simple interest based on user input.
The program should prompt the user to enter the principal amount, the rate
of interest, and the time period in years. It should then compute the simple
interest using the formula Simple Interest= (Principal×Rate×Time) /100
and display the result.'''

print("Finding Simple Interest")
p = float(input("Enter the principle amount:"))
rate = float(input("Enter the rate of interest:"))
t = float(input("Enter the time period in years:"))
SI = (p*rate*t)/100
print(f"SI = {SI}")

