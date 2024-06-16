#!/usr/bin/python3
"""Define a class called square."""


class Square:
    """This is the square class."""

    def __init__(self, size=0, position=(0, 0)):
        """initializing an instance of a square.

        Args:
            size (int): the size of an instance.
            position (tuple): the position of an instance.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter of size property."""
        return self.__size

    @property
    def position(self):
        """Getter of position property."""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter of size property."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter of position property."""
        zero = value[0]
        one = value[1]
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method of the square class.

        Returns:
            int: the area of an instance.
        """
        return self.__size ** 2

    def my_print(self):
        """prints the actual square in #s"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
