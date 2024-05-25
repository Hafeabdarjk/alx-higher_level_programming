#!/usr/bin/python3
def no_c(my_string):
    new_string = [x for x in my_string if x != 'c']
    newer_string = [x for x in new_string if x != 'C']
    for i in newer_string:
            print(i, end = '')
    print()
