#!/usr/bin/python3
def uppercase(str):
    for i in str:
        code = ord(i)
        if code > 96 and code < 123:
            capchr = "{}".format(chr(code-32))
        else:
            capchr = "{}".format(chr(code))
        print(capchr, end='')
    print()
