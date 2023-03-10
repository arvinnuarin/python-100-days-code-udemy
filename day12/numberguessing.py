import random
import art
import os


def result(answer, guess):
    if (guess > answer):
        return "Too high."
    elif (guess < answer):
        return "Too low."
    else:
        return "Correct"


os.system("cls")

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Type 'easy' or 'hard': ").lower()

# Tries
attempts = 0
mynumber = random.randint(1, 100)

if (difficulty != "easy" and difficulty != "hard"):
    print("Please select Easy or Hard.")
    quit(0)

if (difficulty == "easy"):
    attempts = 10
elif (difficulty == "hard"):
    attempts = 5

while (attempts > 0):
    guess = int(input("Make a guess: "))

    guessResult = result(mynumber, guess)

    if (guessResult == "Correct"):
        print(f"Nice! You correctly guessed the number {mynumber}.")
        break
    else:
        attempts -= 1
        print(guessResult)

        if attempts == 0:
            print(
                f"Tssk. You ran out of attempts. Correct number is {mynumber}.")
        else:
            print(f"You have {attempts} remaining to guess the number.")
