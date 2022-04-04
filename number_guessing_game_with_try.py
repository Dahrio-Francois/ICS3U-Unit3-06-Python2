#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program lets you play a number guessing game
#   with user input


import random

some_variable = random.randint(0, 9)


def main():
    # this program starts the game
    integer_as_string = input(
        "Enter an guess (between 0 & 9: "
    )  # a number between 0 & 9
    print("")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        print("You entered an integer correctly")
        if integer_as_string == some_variable:
            print("\nCorrect! You guessed the right number!")
        if integer_as_string != some_variable:
            print("\nIncorrect! The correct number was {}.".format(some_variable))
    except Exception:
        print("This was not an integer")
    finally:
        print("\nTry again?")


if __name__ == "__main__":
    main()
