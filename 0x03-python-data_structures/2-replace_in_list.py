#!/usr/bin/python3

if __name__ == "__main__":
    """Function that replaces an element of a list at a specific position"""


def replace_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return True
