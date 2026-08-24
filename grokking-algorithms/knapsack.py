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
    def __init__(self, maxCapacity) -> None:
        self._stored: List[Item] = []
        self._capacity: int = maxCapacity
        self._value: int = 0
        self._filled: int = 0

    def addItem(self, item: Item):
        if item.weight > self.remainingCapacity:
            raise ValueError(
                f"Incomming item weight ({item.weight}) is greater than capacity ({self.remainingCapacity})"
            )
        self._stored.append(item)
        self._filled += item.weight
        self._value += item.value

    @property
    def stored(self):
        return self._stored

    @property
    def value(self):
        return self._value

    @property
    def filled(self):
        return self._filled

    @property
    def remainingCapacity(self):
        return self._capacity - self.filled

    def __str__(self) -> str:
        return f"Bag(\n\tcapacity={self._capacity},\n\titems={[str(item) for item in self._stored]},\n\tfilled={self.filled},\n\tvalue={self.value}\n)"


def knapsack(items: Dict, maxWeight: int) -> List[List[Bag]]:
    itemsArr = [
        Item(name, items[name]["weight"], items[name]["value"]) for name in items.keys()
    ]
    bagMaxIndex = maxWeight + 1

    # create matrix of empty bags with associated capacity
    m: List[List[Bag]] = []

    prevRow = [Bag(capacity) for capacity in range(1, bagMaxIndex)]

    for curItemIdx, curItem in enumerate(itemsArr):
        newRow = []

        for curBagIdx, curBagCapacity in enumerate(range(1, bagMaxIndex)):
            if curBagCapacity < curItem.weight:
                newRow.append(prevRow[curBagIdx])
                continue

            curBag = Bag(curBagCapacity)
            curBag.addItem(curItem)

            if curBag.remainingCapacity:
                remainderBag = prevRow[curBag.remainingCapacity - 1]
                for item in remainderBag.stored:
                    curBag.addItem(item)

            # ternary would look cooler but would make reading more difficult
            if prevRow[curBagIdx].value < curBag.value:
                newRow.append(curBag)
            else:
                newRow.append(prevRow[curBagIdx])
        m.append(newRow)
        prevRow = newRow
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
