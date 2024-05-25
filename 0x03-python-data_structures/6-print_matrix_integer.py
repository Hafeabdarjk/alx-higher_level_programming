#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for i in rows:
            if i is rows[-1]:
                print("{:d}".format(i), end='')
            else:
                print("{:d}".format(i), end=' ')
        print()
