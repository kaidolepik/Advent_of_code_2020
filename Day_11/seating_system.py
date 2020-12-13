import itertools
import numpy as np

def is_adjacent_in_direction(layout, i, j, direction, look_counter):
    new_i = i + direction[0]
    new_j = j + direction[1]
    counter = 1

    while 0 <= new_i < layout.shape[0] and 0 <= new_j < layout.shape[1] and counter <= look_counter:
        if layout[new_i, new_j] != ".":
            return 1 if layout[new_i, new_j] == "#" else 0

        new_i += direction[0]
        new_j += direction[1]
        counter += 1

    return 0

def count_adjacent(layout, i, j, look_counter):
    adjacent_sum = 0

    for direction in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]: 
        adjacent_sum += is_adjacent_in_direction(layout, i, j, direction, look_counter)

    return adjacent_sum

def generate_layout(layout, look_counter, occupied_criteria):
    new_layout = layout.copy()

    for i, j in itertools.product(range(layout.shape[0]), range(layout.shape[1])):
        if layout[i, j] == ".":
            continue

        adjacent_sum = count_adjacent(layout, i, j, look_counter)

        if layout[i, j] == "L" and adjacent_sum == 0:
            new_layout[i, j] = "#"
        elif layout[i, j] == "#" and adjacent_sum >= occupied_criteria:
            new_layout[i, j] = "L"
    
    return new_layout

def seat_sim(layout, look_counter, occupied_criteria):
    while True:
        new_layout = generate_layout(layout, look_counter, occupied_criteria)

        if np.all(layout == new_layout):
            return layout

        layout = new_layout.copy()


with open("Day_11/input.txt", "r") as fin:
    layout = np.array([list(line.strip()) for line in fin])

print(np.sum(seat_sim(layout, look_counter = 1, occupied_criteria = 4) == "#")) # Day 11.1
print(np.sum(seat_sim(layout, look_counter = max(layout.shape), occupied_criteria = 5) == "#")) # Day 11.2
