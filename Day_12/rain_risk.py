import numpy as np

def navigate_ship(input):
    NSWEF = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0), "F": (1, 0)}
    directions = list(NSWEF.values())[:-1] # The dict key order is maintained in Python 3.7+
    direction = 1 # Start by facing E: (1, 0)
    ship = np.array([0, 0], dtype = int)

    for command, value in input:
        if command in NSWEF:
            ship[0] += NSWEF[command][0] * value
            ship[1] += NSWEF[command][1] * value
        else:
            direction = (direction + int(value/90 if command == "R" else len(directions) - value/90)) % len(directions)
            NSWEF["F"] = directions[direction]

    return ship

def navigate_waypoint(input):
    waypoint = np.array([10, 1], dtype = int)
    ship = np.array([0, 0], dtype = int)
    NSWE = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}

    for command, value in input:
        if command in NSWE:
            waypoint[0] += NSWE[command][0] * value
            waypoint[1] += NSWE[command][1] * value
        elif command == "F":
            ship += waypoint * value
        else:
            theta = np.pi/2 * value/90
            rotation_mat = np.array([[np.cos(theta), np.sin(theta) * (1 if command == "R" else -1)], 
                [np.sin(theta) * (-1 if command == "R" else 1), np.cos(theta)]], dtype = int)

            waypoint = rotation_mat.dot(waypoint)

    return ship


with open("Day_12/input.txt", "r") as fin:
    input = [(line[0], int(line[1:].strip())) for line in fin]

print(np.sum(np.abs(navigate_ship(input)))) # Day 12.1
print(np.sum(np.abs(navigate_waypoint(input)))) # Day 12.2
