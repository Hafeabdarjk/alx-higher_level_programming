#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_list = list(a_dictionary.keys())
    keys_list.sort()
    sorted_dict = {}
    for key in keys_list:
        for x in a_dictionary:
            if x == key:
                print("{}: {}".format(x, a_dictionary[x]))
