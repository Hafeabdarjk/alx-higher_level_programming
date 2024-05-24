#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            capchr = "{}".format(chr(i-32))
        else:
            capchr = "{}".format(chr(i))
        if str[i] != str[-1]:
            print(capchr, end='')
        else:
            print(capchr)
