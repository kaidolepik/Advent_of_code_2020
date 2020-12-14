import numpy as np

def earliest_bus(busses, departure):
    waiting_times = busses - departure % busses

    return np.min(waiting_times) * busses[np.argmin(waiting_times)]

def earliest_timestamp(busses, offsets):
    timetable = busses.copy()

    i = 0
    while i < len(busses) - 1:
        if timetable[i+1] < timetable[i]:
            timetable[i+1] += (int((timetable[i] - timetable[i+1]) / busses[i+1]) + 1 + int(offsets[i] / busses[i+1])) * busses[i+1]
        
        if timetable[i+1] - timetable[i] == offsets[i]:
            i += 1
        else:
            lcm = np.lcm.reduce(busses[:i+1])
            timetable[:i+1] += max(1, int((timetable[i+1] - timetable[i]) / lcm)) * lcm

    return timetable[0]


with open("Day_13/input.txt", "r") as fin:
    departure = int(fin.readline().strip())
    bus_line = fin.readline().strip().split(",")

    busses = np.array([int(bus) for bus in bus_line if bus != "x"], dtype = int)
    offsets = np.diff(np.array([int(i) for i in range(len(bus_line)) if bus_line[i] != "x"], dtype = int))

print(earliest_bus(busses, departure)) # Day 13.1
print(earliest_timestamp(busses, offsets)) # Day 13.2
