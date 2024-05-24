#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        code = ord(str[i])
        if code > 96 and code < 123:
            capchr = "{}".format(chr(code-32))
        else:
            capchr = "{}".format(chr(code))
        if i != len(str) - 1:
            print(capchr, end='')
        else:
            print(capchr)
