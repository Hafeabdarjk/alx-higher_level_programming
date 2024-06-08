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
        """Getter/Setter of size property."""
        return self.__size

    @property
    def position(self):
        """Getter/Setter of position property."""
        return self.__position

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    @position.setter
    def size(self, new_position):
        zero = new_position[0]
        one = new_position[1]
        if (not isinstance(new_position, tuple) or
                len(new_position) != 2 or
                not all(isinstance(num, int) for num in new_position) or
                not all(num >= 0 for num in new_position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = new_position

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
            for x in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
