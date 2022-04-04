#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program lets you play a number guessing game
#   with user input


import random

some_variable = random.randint(0, 9)


def main():
    # this program starts the game

    # process & output
    try:
        guess = int(input("Enter an guess (between 0 & 9: "))  # a number between 0 & 9

        if guess == some_variable:
            print("\nCorrect! You guessed the right number!")

        else:
            print("\nIncorrect! The correct number was {}.".format(some_variable))
    except Exception:
        print("\nThis was not an integer")
    finally:
        print("\nTry again?")


if __name__ == "__main__":
    main()
