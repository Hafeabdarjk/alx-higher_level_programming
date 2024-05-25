#!/usr/bin/python3
def no_c(my_string):
    c_list = [x for x in my_string if x != 'c']
    C_list = [x for x in c_list if x != 'C']
    new_string = ""
    for i in C_list:
        new_string = new_string + i
    return new_string
