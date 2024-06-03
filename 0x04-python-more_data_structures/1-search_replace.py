#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        elemnt = my_list[i]
        if elemnt == search:
            new_list.append(replace)
        else:
            new_list.append(elemnt)
    return new_list
