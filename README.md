# Advent of Code 2020

Participated in [Advent of code](https://adventofcode.com/) for the first time. Used base R, matrix calculations and tidyverse in the beginning; later switched to Python for easier handling of data structures and algorithms, occasionally making use of numpy.

![Advent of Code 2020](images/AoC_2020.png)

### Day 1

It is straightforward to find all the N-element combinations in R using `combn`.

### Day 2

Simple tidyverse solution with some string manipulations.

### Day 3

Put the input into a matrix and queried the cells corresponding to the trajectory.

### Day 4

Parsed the input into a data frame of "individuals x features" by manipulating between long and wide formats. The rest was filtering.

### Day 5

Converting to binary is easy with `strtoi`.

### Day 6

Pure tidyverse; focused on parsing the input to facilitate filtering.

### Day 7

Read the data into a graph, found all possible paths from the starting node (sequence of edges all the way down to leaves), and summed together the number of bags from each path.

### Day 8

Transitioned from R to Python to make the implementation of the puzzle logic clearer.

### Day 9

Numpy can help to reduce the number of lines of code but direct implementation of the puzzle logic can be more efficient and understandable.

### Day 10

Dynamic programming.

### Day 11

Parsed the input into a numpy matrix layout and simulated layouts according to puzzle logic until convergence.

### Day 12

In part 2, used rotation matrix to calculate after-rotation waypoint positions with reference to the origin/ship. In part 1, rotated the ship at the origin rather bluntly – would have been easier to keep track of the degrees of rotation and use `math.cos(math.radians(degrees))` for the E-W direction and `math.sin(math.radians(degrees))` for the N-S direction.

### Day 13

Did not know about it but turns out I implemented the Chinese remainder theorem.

### Day 14

Used a queue (FIFO) to create all possible bitstrings: each "X" in a bitstring was replaced by 1/0, creating two new bitstrings; the original was popped and the new appended.

### Day 15

Used dictionaries to keep track of how many times and when each number occurred.

### Day 16

Found all valid fields for every position; if there was only a single valid field then marked it down and eliminated it from further queries. Repeated until all fields had a single match.

### Day 17

Created a matrix with pre-calculated dimensions and used `numpy.roll` to calculate the number of neighbours.

### Day 18

Wrapped the entire expression in parentheses and solved recursively by starting from the deepest level until there were no parentheses remaining.

### Day 19

Found all possible messages that rules could match by recursively going deeper in the tree of rules. Complemented the rules to allow for loops using string manipulations and used regex to search for messages matching any of the rules.

### Day 20

Matched tiles by edge, then oriented the tiles and put them into place starting from the top-left corner (moved left to right in a top-down approach).

### Day 21

Found possible ingredients for all allergens using set intersections, then made sure only a single match remained by removing single matches found previously.

### Day 22

A straightforward recursive algorithm to implement the puzzle logic.

### Day 23

Used an abstract linked list implemented using a dictionary – each number represents a key in the dictionary whose value is the next number in the sequence (in hindsight, could have simply used an array where the N-th element contains the number in the sequence following the number N). Updating the sequence was thus a constant time operation.

### Day 24

The same solution as in Day 17, only in 2D this time (hexagonal tiles can be represented in 2D coordinates).

### Day 25

Straightforward implementation of the puzzle logic.
