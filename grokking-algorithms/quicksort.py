#!/usr/bin/env python3

import random

random.seed(9)


def quicksort(arr):
    arrLen = len(arr)
    if arrLen < 2:
        return arr

    pivotIndex = random.randint(0, arrLen - 1)

    less = [elem for elem in arr if arr[pivotIndex] > elem]
    more = [elem for elem in arr if arr[pivotIndex] < elem]
    equal = [elem for elem in arr if arr[pivotIndex] == elem]

    return quicksort(less) + equal + quicksort(more)


print(quicksort([random.randint(0, 10000) for _ in range(0, 100000)]))
