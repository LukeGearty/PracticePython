#!/usr/bin/python3
import sys
import random
### a function to get the computer guess ##
def computer_guess():
    guess = random.randint(1000,10000)
    return guess
## a function to get the user guess ##
def user_guess():
    user_num = input("Give me a 4 digit number: ")
    if len(user_num) != 4:
        print("Invalid input, try again")
        user_num = input("Give me a 4 digit number: ")
    return user_num
## The function to compare the numbers ##
def cows_bulls():
    computer = str(computer_guess())
    play = True
    guesses = 0
    while play:
        user = user_guess()
        cows = 0
        bulls = 0
        guesses += 1
        if user != computer:
            for num in range(0,4):
                if user[num] == computer[num]:
                    cows += 1
                    print(f"{user[num]} is a cow")
                if user[num] in computer and user[num] != computer[num]:
                    bulls += 1
                    print(f"{user[num]} is a bull")
            print(f"Cow Count: {cows}")
            print(f"Bull Count: {bulls}")
            print("Try again!")
        if user == computer:
            print(f"Good job! The number was {computer} and you guessed it right in {guesses} guesses!")
            play = False
        elif user == 'exit':
            print(f"The number was {computer}")
            play = False
        elif guesses == 5:
            print(f"The number was {computer}! Try again")
            play = False
def main():
    print("Let's play a game!")
    print("I will think of a random number, and so while you")
    print("For every number that you guess that is in the right place, you get a cow.")
    print("For every number that you guess that is in my number, but in the wrong place, you get a bull")
    print("If you guess 5 times and you can't get it, then I'll give you the number")
    print("Let's Play!")
    cows_bulls()
if __name__ == "__main__":
    main()
