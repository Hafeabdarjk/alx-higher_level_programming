#!/usr/bin/python3
"""Define a class called square."""


class Square:
    """This is the square class."""

    def __init__(self, size=0):
        """initializing an instance of a square.

        Args:
            size (int): the size of an instance.
        """
        self.__size = size

    @property
    def size(self):
        """Getter of size property."""
        return self.__size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        """Public instance method of the square class.

        Returns:
            int: the area of an instance.
        """
        return self.__size ** 2
