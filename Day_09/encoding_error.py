import itertools
import numpy as np

def invalid_number(numbers, k = 25):
    for i in range(k, len(numbers)):
        if numbers[i] not in [left + right for left, right in itertools.combinations(numbers[i-k:i], 2)]:
            return numbers[i]

def encryption_weakness_short(numbers, invalid):
    cum_sum = np.cumsum(numbers)
    ix = np.where(cum_sum - cum_sum[:, np.newaxis] == invalid)

    return min(numbers[ix[0][0]+1:ix[1][0]+1]) + max(numbers[ix[0][0]+1:ix[1][0]+1])

def encryption_weakness_efficient(numbers, invalid):
    i, j, cum_sum = (0, 0, 0)

    while cum_sum != invalid:
        if cum_sum < invalid:
            cum_sum += numbers[j]
            j += 1
        else:
            cum_sum -= numbers[i]
            i += 1

    return min(numbers[i:j]) + max(numbers[i:j])


with open("Day_09/input.txt", "r") as fin:
    numbers = [int(line.strip()) for line in fin]
    
invalid = invalid_number(numbers); print(invalid) # Day 9.1
print(encryption_weakness_short(numbers, invalid)) # Day 9.2 (short code)
print(encryption_weakness_efficient(numbers, invalid)) # Day 9.2 (efficient code)
