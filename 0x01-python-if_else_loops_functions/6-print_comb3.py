#!/usr/bin/python3
for i in range(9):
    n = i+1
    for j in range(n, 10):
        number = "{}{}, ".format(i,j)
        last_number = "{}{}".format(i,j)
        if i == 8 and j == 9:
            print(last_number)
        else:
            print(number, end='')
