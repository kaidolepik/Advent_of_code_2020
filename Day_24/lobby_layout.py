import re
import numpy as np
from collections import defaultdict

directions = {"e": (1, 0), "se": (1, 1), "sw": (0, 1), "w": (-1, 0), "nw": (-1, -1), "ne": (0, -1)}

def tile_layout(sequences):
    layout = defaultdict(bool)

    for sequence in sequences:
        tile = np.array((0, 0))
        for direction in sequence:
            tile = tile + directions[direction]
        
        layout[tuple(tile)] = not layout[tuple(tile)]

    return layout

def exhibition(layout, day):
    max_tile = max([max(np.abs(key)) for key in layout.keys()])

    pocket = np.full([2 * (day+max_tile+1)] * 2, False)
    for key, value in layout.items():
        pocket[tuple(np.array(key) + day+max_tile+1)] = value

    for _ in range(day):
        blacks = sum(np.roll(pocket, neighbour, axis = (0, 1)) for neighbour in directions.values())
        pocket = np.where(pocket*(blacks == 1) + pocket*(blacks == 2) + (pocket == False)*(blacks == 2), True, False)

    return pocket


with open("Day_24/input.txt", "r") as fin:
    sequences = [list(filter(None, re.split("(" + "|".join(directions.keys()) + ")", sequences))) for sequences in fin.read().strip().split("\n")]

# Day 24.1
layout = tile_layout(sequences)
print(sum(layout.values()))

# Day 24.2
print(np.sum(exhibition(layout, 100)))
