#!/usr/bin/python3

if __name__ == "__main__":
    """Function that prints all integers of a list"""


def print_list_integer(my_list=[]):
    for x in range(len(my_list)):
        print("{:d}".format(my_list[x]))
