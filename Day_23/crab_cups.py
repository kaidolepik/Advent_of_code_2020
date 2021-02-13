def game(numbers, n):
    min_number = min(numbers)
    max_number = max(numbers)
    chain = {key: value for key, value in zip(numbers, numbers[1:] + [numbers[0]])}

    current = numbers[0]
    for _ in range(n):
        clockwise = [chain[current], chain[chain[current]], chain[chain[chain[current]]]]
        destination = current - 1 if current > min_number else max_number
        while destination in clockwise:
            destination = destination - 1 if destination > min_number else max_number

        chain[current] = chain[clockwise[-1]]
        chain[clockwise[-1]] = chain[destination]
        chain[destination] = clockwise[0]

        current = chain[current]

    return chain


with open("Day_23/input.txt", "r") as fin:
    numbers = [int(number) for number in fin.read().strip()]

# Day 23.1
chain = game(numbers, 100)
sequence = [chain[1]]
while len(sequence) < len(numbers) - 1:
    sequence.append(chain[sequence[-1]])
print("".join(str(number) for number in sequence))

# Day 23.2
numbers += list(range(max(numbers) + 1, 1000001))
chain = game(numbers, 10000000)
print(chain[1] * chain[chain[1]])
