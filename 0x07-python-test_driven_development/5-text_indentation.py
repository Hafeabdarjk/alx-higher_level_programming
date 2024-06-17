#!/usr/bin/python3
"""A module with a function for seperating sentances
based on special sympols.
"""


def text_indentation(text):
    """ function for seperating sentances based on special sympols (. / ? / :).

    Args:
        text (str): text to be indented.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text) and text[i] == " ":
        i += 1
    while i < len(text):
        print(text[i], end='')
        if text[i] in ":?." or text[i] == "\n":
            if text[i] in ":?.":
                print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            i += 1
