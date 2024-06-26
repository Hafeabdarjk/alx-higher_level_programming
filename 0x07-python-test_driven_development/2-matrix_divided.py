#!/usr/bin/python3
"""A module with one function for diving matrix elements by a number."""


def matrix_divided(matrix, div):
    """ Divide function elemnts by div which can be integer or float

    Args:
        matrix (list of lists): should contain integers or float numbers
        div (int or float): the number that matrix elements are divided by
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(x, int) or isinstance(x, float))
                    for x in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        " integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[(round((x / div), 2)) for x in row] for row in matrix]
