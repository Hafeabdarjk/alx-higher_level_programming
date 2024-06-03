#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_tuple = tuple(my_list)
    sum = 0
    for x in new_tuple:
        sum += x
    return sum
