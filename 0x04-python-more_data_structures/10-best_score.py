#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    values = list(a_dictionary.values())
    values.sort()
    biggest_value = values[-1]
    for key in a_dictionary:
        if a_dictionary[key] == biggest_value:
            return key
