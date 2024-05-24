#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if chr(str[i]) > 96 and chr(str[i]) < 123:
            capchr = "{}".format(ord(i-32))
        else:
            capchr = "{}".format(ord(i))
        if str[i] != str[-1]:
            print(capchr, end='')
        else:
            print(capchr)
