#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Sept 2019
# This is program prints all numbers form 1000 to 2000 in 5 numbers per line


def temperature():
    # This converts celsius to fahrenheit
    try:
        # input
        celsius = int(input("What is the temperature (c°): "))

        # process
        fahrenheit = (celsius * 1.8) + 32

        # output
        print("The temperature in Fahrenheit is " + str(fahrenheit) + "°")
    except ValueError:
        print("Please enter a integer ")


def main():
    temperature()


if __name__ == "__main__":
    main()
