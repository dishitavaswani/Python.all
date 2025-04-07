'''
Sorting City Names from File: Write a python code to take a file which
contains city names on each line. Alphabetically sort the city names and
write it in another file.
 or
Write a python code to take a file which contains city names on each line.
Alphabetically sort the city names and write it in another file.
'''
with open("cities.txt", "r") as file:
    data = file.read()
    
    cities = data.split("\n")
    cities.sort()

    for city in cities:
        print(city)


with open("cities.txt", "r") as file:
    cities = file.readlines()
    
    cities.sort()

with open("file2.txt", "w") as file:
    for city in cities:
        file.write(city)
