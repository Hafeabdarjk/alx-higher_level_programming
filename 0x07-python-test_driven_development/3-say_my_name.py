#!/usr/bin/python3
"""A module with one function for printing out names."""


def say_my_name(first_name, last_name=""):
    """ Helps you print a sentance "My name is <first name> <last name>"
    based on arguments.

    Args:
        first_name (str): mandatory and have no default value.
        last_name (str): optional and have default value ("")
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
