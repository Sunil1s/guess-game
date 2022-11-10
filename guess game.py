import random
number=random.randint(1,100)
attempt=1
guess= int(input("Enter the number: "))
while(True):
    if guess>number:
        guess=int(input("The guess number is too big Guess another number:"))
        attempt+=1
    elif guess<number:
        guess=int(input("Guess number is small Guess another number"))
        attempt+=1
    else:
        print(f"Yeah that the number! You guesses it {attempt} attempts")  
        break      
