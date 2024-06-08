#!/usr/bin/python3
"""Define a class called square."""


class Square:
    """This is the square class."""

    def __init__(self, size=0):
        """initializing an instance of a square.

        Args:
            size (int): the size of an instance.
        """

        if size is not int:
            raise TypeError("size must be an integer")
            self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
