import numpy as np
import itertools

def active_cubes(input, ndim, cycles):
    n = len(input)
    center = cycles + int(n/2)

    pocket = np.full([n + 2*cycles] * ndim, ".", dtype = str)
    pocket[tuple([slice(center, center+1)]*(ndim-2) + [slice(cycles, cycles+n)]*2)] = input

    neighbours = [np.array(neighbour) for neighbour in itertools.product([-1, 0, 1], repeat = ndim) if neighbour != tuple([0]*ndim)]

    cycle = 0
    while cycle < cycles:
        counts = np.zeros(pocket.shape, dtype = int)
        for neighbour in neighbours:
            counts += np.roll(pocket, neighbour, axis = tuple(range(ndim))) == "#"

        pocket = np.where((pocket == ".")*(counts == 3) + (pocket == "#")*(counts == 2) + (pocket == "#")*(counts == 3), "#", ".")
        cycle += 1

    return pocket


with open("Day_17/input.txt", "r") as fin:
    input = np.array([list(line.strip()) for line in fin], dtype = str)

print(np.sum(active_cubes(input, ndim = 3, cycles = 6) == "#")) # Day 17.1
print(np.sum(active_cubes(input, ndim = 4, cycles = 6) == "#")) # Day 17.2
