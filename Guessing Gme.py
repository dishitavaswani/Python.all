#Write a program that picks a random integer from 1 to 100, and has players guess the number.
import random 
x=random.randint(1,100)
print('Welcome to my 1st game!!!')
print('Some basic rules you should keep in mind before starting')
print("All You gotta do is Guess the number I'm thinking")
print("Let's see if you can guess the Number")
print("I'm thinking of a number between 1-100")
print("If your guess is farther than the last one,I'll say you're getting colder")
print("If your guess is closer than the last one,I'll say you're getting warmer")
print("LET'S PLAY!!!")
guesses=[0]
print("I'm thinking of a number between 1-100")
while True:
    guess=int(input("What's your guess??"))
    if guess < 1 or guess >100:
        print('OUT OF BOUNDS! TRY AGAIN')
        continue
    if guess == x:
        print(f'CONGRATULATIONS!!!,YOU READ MY MIND. YOU GUESSED IT IN ONLY {len(guesses)} GUESSESS!!')
        break
#if guess is incorrect add guess too the list
    guesses.append(guess)
    if guesses[-2]:
        if abs(x-guess)< abs(x-guesses[-2]):
            print('WARMER!')
        else:
            print('COOLER!')
    else:
        if abs(x-guess)<= 10:
            print('WARM!')
        else:
            print('COOL!')
            
            
        
    
    
    
