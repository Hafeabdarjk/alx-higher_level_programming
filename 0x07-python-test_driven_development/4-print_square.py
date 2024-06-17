#!/usr/bin/python3
"""A module with one function for printing a "square"."""


def print_square(size):
    """ Helps you print a square in #s based on size argument.

    Args:
        size (int): the size length of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end='')
        print("")

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")
