with open("names.txt", "r") as file:
    data = file.read()
    
    words = data.split(" ")

    length = int(input("Enter the word length: "))

    for word in words:
        if (len(word) == length):
            print(word)

print("Done!")
