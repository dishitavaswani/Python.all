'''Write a Python program to calculate the gross salary of an employee. The
program should prompt the user for the basic salary (BS) and then compute
the dearness allowance (DA) as 70% of BS, the travel allowance (TA) as
30% of BS, and the house rent allowance (HRA) as 10% of BS. Finally, it
should calculate the gross salary as the sum of BS, DA, TA, and HRA and
display the result.'''


BS = float(input("Enter the basic salary:"))
DA = 0.7 * BS
TA = 0.3 * BS
HRA = 0.1 * BS
Gross_Salary = BS + DA + TA + HRA
print(f"Gross Salary = {Gross_Salary}")
