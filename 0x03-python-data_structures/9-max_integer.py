#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list = []
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for num in range my_list[1:]:
        if my_list[num] > max:
            max = my_list[num]
    return max
