import itertools
import numpy as np

def invalid_number(numbers, k = 25):
    for i in range(k, len(numbers)):
        if numbers[i] not in [left + right for left, right in itertools.combinations(numbers[i-k:i], 2)]:
            return numbers[i]

def encryption_weakness(numbers, invalid):
    for i in range(len(numbers)):
        cum_sum = np.cumsum(numbers[i:]).tolist()
        if invalid in cum_sum:
            return min(numbers[i:i+cum_sum.index(invalid)]) + max(numbers[i:i+cum_sum.index(invalid)])


with open("Day_09/input.txt", "r") as fin:
    numbers = [int(line.strip()) for line in fin]
    
invalid = invalid_number(numbers); print(invalid) # Day 9.1
print(encryption_weakness(numbers, invalid)) # Day 9.2
