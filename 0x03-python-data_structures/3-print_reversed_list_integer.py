#!/usr/bin/python3

if __name__ == "__main__":
    """Function that prints in reverse"""


def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for x in range(len(my_list)):
            print("{:d}".format(my_list[x]))
