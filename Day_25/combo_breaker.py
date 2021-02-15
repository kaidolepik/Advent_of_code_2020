def key_operation(key_value, subject_number):
    return (key_value * subject_number) % 20201227

def determine_encryption_key(subject_number, loop_size, key_value = 1):
    for _ in range(loop_size):
        key_value = key_operation(key_value, subject_number)

    return key_value

def determine_loop_size(public_key, subject_number = 7, key_value = 1):
    loop_size = 0
    while key_value != public_key:
        key_value = key_operation(key_value, subject_number)

        loop_size += 1

    return loop_size


with open("Day_25/input.txt", "r") as fin:
    public_keys = [int(key) for key in fin.read().strip().split("\n")]

# Day 25
loop_sizes = [determine_loop_size(public_key) for public_key in public_keys]
print(determine_encryption_key(public_keys[0], loop_sizes[1]))
print(determine_encryption_key(public_keys[1], loop_sizes[0]))
