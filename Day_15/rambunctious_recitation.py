from collections import defaultdict

def nth_number(n):
    count = defaultdict(int)
    pos = defaultdict(list)

    with open("Day_15/input.txt", "r") as fin:
        for i, number in enumerate([int(number) for number in fin.read().strip().split(",")]):
            count[number] += 1
            pos[number] += [i]

    for i in range(sum(count.values()), n):
        number = 0 if count[number] == 1 else pos[number][-1] - pos[number][-2]
        count[number] += 1
        pos[number] += [i]

    return(number)


print(nth_number(2020)) # Day 15.1
print(nth_number(30000000)) # Day 15.2
