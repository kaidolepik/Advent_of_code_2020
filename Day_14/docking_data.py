from collections import defaultdict, deque

def docking_program_1(docking, command, value, mask):
    bitstring = "".join([mem_char if mask_char == "X" else mask_char for mem_char, mask_char in zip(format(int(value), "036b"), mask)])
    docking[int(command.replace("mem[", "").replace("]", ""))] = int(bitstring, base = 2)

    return docking

def docking_program_2(docking, command, value, mask):
    address = format(int(command.replace("mem[", "").replace("]", "")), "036b")
    queue = deque(["".join([adr_char if mask_char == "0" else mask_char for adr_char, mask_char in zip(address, mask)])])
    
    while "X" in queue[0]:
        queue.append(queue[0].replace("X", "0", 1))
        queue.append(queue.popleft().replace("X", "1", 1))

    for bitstring in queue:
        docking[int(bitstring, base = 2)] = int(value)

    return docking

def initialize_docking(program_version):
    mask = ""
    docking = defaultdict(int)

    with open("Day_14/input.txt", "r") as fin:
        for line in fin:
            command, value = line.strip().split(" = ")

            if command.startswith("mask"):
                mask = value
            else:
                docking = docking_program_1(docking, command, value, mask) if program_version == 1 else docking_program_2(docking, command, value, mask)

    return sum(docking.values())


print(initialize_docking(program_version = 1)) # Day 14.1
print(initialize_docking(program_version = 2)) # Day 14.2
