#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: April 2021
# This program is a better guessing number game

import random


def main():
    print("Try to guess a number from 0 to 9:")

    number_input = int(input())
    number_random = random.randint(0, 9)

    if number_input == number_random:
        print("\nCongratulations, guessed right!")
    else:
        print("\nSorry, guessed wrong! The right number was {}"
              .format(number_random))

    print("\nDone.")


if __name__ == "__main__":
    main()
