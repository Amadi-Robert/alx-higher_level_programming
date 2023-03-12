#!/usr/bin/python3

if __name__ == "__main__":
    """Function that retrieves an element from a list"""


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))
