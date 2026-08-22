#!/usr/bin/env python3

import random

random.seed(9)


def merge(left, right):
    res = []
    while left or right:
        l = left[0] if left else None
        r = right[0] if right else None
        if l is not None and (r is None or l < r):
            res.append(l)
            left.pop(0)
        else:
            res.append(r)
            right.pop(0)
    return res


def mergesort(arr):
    arrLen = len(arr)
    if arrLen <= 1:
        return arr

    midpoint = int(arrLen / 2)
    left = arr[:midpoint]
    right = arr[midpoint:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


print(mergesort([random.randint(0, 10000) for _ in range(0, 100000)]))
