#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [x**2 for rows in matrix for x in rows]
    print(new_matrix)
