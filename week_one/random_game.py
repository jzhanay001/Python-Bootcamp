# import the random module
import random

winning_number = random.randint(0,100)
print(winning_number)

num_guesses = 10
user_won = False
numtry=0
guess=[]

while num_guesses != 0 and user_won == False:
    user_guess = int(input("Enter your guess: "))
    guess.append(user_guess)

    if user_guess == winning_number:
        print("Hey, you won!")
        user_won = True
        numtry=numtry+1
    elif user_guess >= (winning_number-5) and user_guess <= (winning_number+5):
        num_guesses -= 1
        numtry=numtry+1
        if num_guesses == 0:
            print("Nope, you lost.")
        else:
            print ("HOT")
            print("Nope, try again.")
    elif user_guess >= (winning_number-10) and user_guess <= (winning_number+10):
        num_guesses -= 1
        numtry=numtry+1
        if num_guesses == 0:
            print("Nope, you lost.")
        else:
            print ("WARM")
            print("Nope, try again.")
    else:
        num_guesses -= 1
        numtry=numtry+1
        if num_guesses == 0:
            print("Nope, you lost.")
        else:
            print("COLD")
            print("Nope, try again.")
print("Number of tries", numtry)
print("Guesses", guess)
