#Write a program to count the frequency of each character in a string.
a=str(input('Enter a String:'))
freq={}
for char in a:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
