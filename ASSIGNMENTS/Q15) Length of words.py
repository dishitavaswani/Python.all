''' Develop a Python program that reads a text file and prints words of
specified lengths (e.g., three, four, five, etc.) found within the file.'''

file = open("names.txt","r") 
max_len = 0

text = file.read()
words = text.split(" ")
for words in words:
    if(len(words)>=max_len):
        max_len = len(words)
        length=int(input("Enter the desired word length:"))
        wordinfile=[word for words in words if len(words)==length]
        if wordinfile:
            print(f'words of length {length} ')
            for words in wordinfile:
                print(word)
        else:
            print(f'No words of length {length}')
            
file.close()
