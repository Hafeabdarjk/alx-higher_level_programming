#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)-1):
        chrc = my_string[i]
        if i == 'c' or "C":
            continue
        elif i == len(my_string) - 1:
            print(i)
        else:
            print(i, end='')
