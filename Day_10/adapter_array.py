import numpy as np

def N_arrangements(diff):
    dynamic = np.ones(len(diff), dtype = np.int64)

    for i in range(1, len(dynamic)):
        prev3_to_i = (3 - sum(diff[i-3:i]) >= 0) if i >= 3 else False
        prev2_to_i = (3 - sum(diff[i-2:i]) >= 0) if i >= 2 else False

        dynamic[i] = dynamic[i-1] + dynamic[i-2]*prev2_to_i + dynamic[i-3]*prev3_to_i

    return dynamic[-1]


with open("Day_10/input.txt", "r") as fin:
    numbers = [int(line.strip()) for line in fin]

# Day 10.1
diff = np.diff(np.sort(numbers + [0, max(numbers)+3]))
print(sum(diff == 1) * sum(diff == 3))

# Day 10.2
print(N_arrangements(diff))
