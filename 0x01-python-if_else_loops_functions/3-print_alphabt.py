#!/usr/bin/python3
for i in range(97, 123):
    if i in [101, 113]:
        continue
    letter = chr(i)
    print("{}".format(letter), end='')
