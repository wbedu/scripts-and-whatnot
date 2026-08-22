#!/usr/bin/env python3

# Chapter 11 of grokking algo book

from typing import Dict, List


class Item:
    def __init__(self, name, weight, value):
        self._name = name
        self._weight = weight
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"""{self.name}::{self.value}::{self.weight}"""


class Bag:
    def __init__(self, capacity) -> None:
        self._stored: List[Item] = []
        self._capacity: int = capacity

    def addItem(self, item: Item):
        if item.weight > self.capacity:
            raise ValueError(
                f"Incomming item weight ({item.weight}) is greater than capacity ({self.capacity})"
            )
        # Will throw even if two distinct items have the same name
        # not in scope for this exercise
        if self.isContainsItem(item):
            raise AssertionError("Cannot have the same item more than once")
        self._stored.append(item)

    def isContainsItem(self, item: Item):
        return item.name in [i.name for i in self.stored]

    @property
    def stored(self):
        return self._stored

    @property
    def value(self):
        return sum([item.value for item in self.stored])

    @property
    def filled(self):
        return sum([item.weight for item in self.stored])

    @property
    def capacity(self):
        return self._capacity - self.filled

    def __str__(self) -> str:
        return f"Bag(\n\tcapacity={self._capacity},\n\titems={[str(item) for item in self._stored]},\n\tfilled={self.filled},\n\tvalue={self.value}\n)"


def knapsack(items: Dict, maxWeight: int) -> List[List[Bag]]:
    itemsArr = [
        Item(name, items[name]["weight"], items[name]["value"]) for name in items.keys()
    ]
    bagMaxIndex = maxWeight + 1
    itemMaxIndex = len(itemsArr)

    # create matrix of empty bags with associated capacity
    m = [
        [Bag(capacity) for capacity in range(1, maxWeight + 1)]
        for _ in range(0, itemMaxIndex)
    ]

    for curItemIdx, row in enumerate(m):
        curItemValue = itemsArr[curItemIdx]
        prevIdx = curItemIdx - 1
        for curBagIdx, curBagValue in enumerate(row):
            if curBagValue.capacity >= curItemValue.weight:
                curBagValue.addItem(curItemValue)
            if curBagValue.capacity:
                closestMatchBag = m[prevIdx][curBagValue.capacity - 1]
                for item in closestMatchBag.stored:
                    curBagValue.addItem(item)

            # ternary would look cooler but would make reading more difficult
            if m[prevIdx][curBagIdx].value < curBagValue.value:
                m[curItemIdx][curBagIdx] = curBagValue
            else:
                m[curItemIdx][curBagIdx] = m[prevIdx][curBagIdx]
    return m


items = {
    "guitar": {"weight": 1, "value": 1500},
    "stereo": {"weight": 4, "value": 3000},
    "laptop": {"weight": 3, "value": 2000},
    "phone": {"weight": 1, "value": 2000},
}

maxWeight = 4

res = knapsack(items, maxWeight)


print("\nvalue matrix")
for row in res:
    for bag in row:
        print(bag.value, end=" ")
    print("\n")
print("Optimal bag\n", res[-1][-1], sep="")
