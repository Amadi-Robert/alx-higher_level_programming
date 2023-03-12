#!/usr/bin/python3
if __name__ == "__main__":


def new_in_list(my_list, idx, element):
    copy = list(my_list)
    if idx < 0 or idx > len(my_list) - 1):
        return copy
    else:
        copy[idx] = element
	return copy
