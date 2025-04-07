# Write to the file
with open('myfile.txt', mode='w') as f:
    f.write('my first file!')

# Read from the file
with open('myfile.txt', mode='r') as f:
    print(f.read())

# Append to the file
with open('myfile.txt', mode='a') as f:
    f.write('This is line 2')

# Read from the file again
with open('myfile.txt', mode='r') as f:
    print(f.read())
