#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        number = "0{}, ".format(i)
    elif i < 99:
        number = "{}, ".format(i)
    else:
        number = "{}".format(i)
    if i < 99:
        print(number, end='')
    else:
        print(number)
