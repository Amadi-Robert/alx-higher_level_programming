#!/usr/bin/python3

def no_c(my_string):
    char_to_remove = ['c', 'C']
    for char in char_to_remove:
        while char in string:
            my_string.remove(char)
            return my_string
