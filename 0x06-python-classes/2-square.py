#!/usr/bin/python3
"""Define a class called square."""


class Square:
    """This is the square class."""

    def __init__(self, size=0):
        """initializing an instance of a square.

        Args:
            size (int): the size of an instance.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  
