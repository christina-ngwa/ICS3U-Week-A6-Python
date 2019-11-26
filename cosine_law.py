#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: November 2019
# This is program is a cosine law calculator

import math


def cosine_law(a, b, angle_c):
    # This function calculates the side of a triangle

    # process
    c_squared = round(math.sqrt(pow(a, 2) + pow(b, 2) - ((2)*(a)*(b)
                      (*(math.cos(math.radians(angle_c))))), 2))

    return c_squared


def main():

    # input
    print("Welcome to the Cosine Law calculator.")
    print("")
    a_try = input("Enter value of side a: ")
    try:
        a = float(a_try)
        b_try = input("Enter value of side b: ")
        try:
            b = float(b_try)
            angle_c_try = input("Enter value of angle C (degrees): ")
            try:
                angle_c = float(angle_c_try)

                # call function
                c = cosine_law(a, b, angle_c)

                # output
                print("")
                print("The value of side c is {} .".format(c))

            except Exception:
                print("Wrong input. Try again.")
        except Exception:
            print("Wrong input. Try again.")
    except Exception:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()
