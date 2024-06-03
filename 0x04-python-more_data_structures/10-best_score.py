#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == {}:
        return None
    biggest_value = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == biggest_value:
            return key
