def console_execution(instructions):
    visited = set()
    acc = 0
    line = 0

    while line not in visited and line < len(instructions):
        visited.add(line)
        command, value = instructions[line]

        if command == "acc":
            acc += int(value)

        line += int(value) if command == "jmp" else 1

    return (line >= len(instructions), acc)

def repaired_console_acc(instructions):
    for line in instructions:
        command = line[0]
        if command == "acc":
            continue
        line[0] = "nop" if command == "jmp" else "jmp"

        is_executable, acc = console_execution(instructions)
        if is_executable:
            return acc
            
        line[0] = command


with open("Day_08/input.txt", "r") as fin:
    instructions = [(line.strip().split(" ")) for line in fin]

print(console_execution(instructions)[1]) # Day 8.1
print(repaired_console_acc(instructions)) # Day 8.2
