#!/usr/bin/env.python3

# created by: Patrice Pat-Odita
# Created on: oct 21 2022
# This program compares floating point numbers
# using if else statement and user input


def compareFloatNum(Float1input, Float2input):
    if Float1input == Float2input:
        print(("\033[1;35;34mThe numbers are equal"))
    else:
        print(("\033[1;35;35mThe numbers are not equal"))


# Driver code


def main():
    while True:
        uinput1 = input("Enter a number: ")

        try:
            uflt1 = float(uinput1)
            break
        except:
            print(("\033[1;35;35mThat isn't a number..."))

    while True:
        uinput2 = input("Enter another number: ")

        try:
            uflt2 = float(uinput2)
            break
        except:
            print(("\033[1;35;34mThat isn't a number"))

    compareFloatNum(uflt1, uflt2)


if __name__ == "__main__":
    main()
