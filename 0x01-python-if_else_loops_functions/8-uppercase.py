#!/usr/bin/python3
def uppercase(str):
    for i in str:
        code = ord(i)
        if code > 96 and code < 123:
            capchr = "{}".format(chr(code-32))
        else:
            capchr = "{}".format(chr(code))
<<<<<<< HEAD
        print(capchr, end='')
    print()
=======
        if i == len(str) - 1 or str[i] == "":
            print(capchr)
        else:
            print(capchr, end='')
>>>>>>> dfd94b7ecb8df3421d5d0ea8c9079eb2b831650e
