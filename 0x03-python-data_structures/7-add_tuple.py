#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a1 = a2 = 0
    elif len(tuple_a) == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1, a2 = tuple_a
    if len(tuple_b) == 0:
        b1 = b2 = 0
    elif len(tuple_b) == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1, b2 = tuple_b
    x = a1 + b1
    z = a2 + b2
    tuple_sum = (x, z)
    return tuple_sum
