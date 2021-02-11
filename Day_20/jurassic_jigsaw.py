import numpy as np
import itertools
from collections import deque
import re

class Tile:
    def __init__(self, tile_info):
        lines = tile_info.strip().split("\n")

        self.ID = int(lines[0].split(" ")[1][:-1])
        self.image = np.array([list(line) for line in lines[1:]], dtype = "<U1")
        self.neighbors = deque([[], [], [], []]) # 0=top, 1=right, 2=bottom, 3=left

    def edges(self):
        return [self.image[0, :], self.image[:, -1], self.image[-1, :][::-1], self.image[:, 0][::-1]] # 0=top, 1=right, 2=bottom, 3=left

    def rotate(self):
        self.image = np.array(list(zip(*reversed(self.image))), dtype = "<U1") # Clockwise rotation of the image
        self.neighbors.rotate()

    def flip(self):
        self.image = self.image.transpose()
        self.neighbors.reverse()


def set_neighbors(tiles):
    for tileA, tileB in itertools.combinations(tiles, 2):
        for (keyA, edgeA), (keyB, edgeB) in itertools.product(enumerate(tileA.edges()), enumerate(tileB.edges())):
            if np.all(edgeA == edgeB) or np.all(edgeA[::-1] == edgeB):
                tileA.neighbors[keyA].append(tileB)
                tileB.neighbors[keyB].append(tileA)

def match_tile(tile, left, top):
    for _ in range(2):
        for _ in range(4):
            # If (there is no left neighbor or the left edge equals value) and (there is no top neighbor or the top edge equals value)
            if ((len(tile.neighbors[3]) == 0 and len(left) == 0) or (len(left) != 0 and np.all(tile.edges()[3][::-1] == left))) and ((len(tile.neighbors[0]) == 0 and len(top) == 0) or (len(top) != 0 and np.all(tile.edges()[0][::-1] == top))):
                return tile
            tile.rotate()
        tile.flip()

def build_image_board(tiles):
    N = int(np.sqrt(len(tiles)))
    board = [[None for _ in range(N)] for _ in range(N)] # NxN board

    # Fill the board with tiles from left to right, from top to bottom
    for i, j in itertools.product(range(N), range(N)):
        left = [] if j == 0 else board[i][j-1].edges()[1]
        top = [] if i == 0 else board[i-1][j].edges()[2]
        # Corner tile at the start; bottom neighbor of the top tile at new column; otherwise right neighbor of the left tile
        tile = corners[0] if i == 0 and j == 0 else (board[i-1][j].neighbors[2][0] if j == 0 else board[i][j-1].neighbors[1][0])

        board[i][j] = match_tile(tile, left, top)

    # Remove borders and create a matrix from the blocks
    return np.block([[tile.image[1:-1, 1:-1] for tile in tiles] for tiles in board])

def orient_to_monsters(board, monster_shape):
    # Originally used individual regexes for each line in the monster and summed the matches that aligned; a single regex is neater, though
    monster_regex = "(?=(" + (".{" + str(board.shape[1] - len(monster_shape[0]) + 1) + "}").join(monster_shape) + "))"

    for _ in range(2):
        for _ in range(4):
            N_monsters = len(re.findall(monster_regex, "-".join(["".join(row) for row in board])))
            if N_monsters > 0:
                return board, N_monsters

            board = np.array(list(zip(*reversed(board))), dtype = "<U1")
        board = board.transpose()


with open("Day_20/input.txt", "r") as fin:
    tiles = [Tile(tile_info) for tile_info in fin.read().split("\n\n")]

# Day 20.1
set_neighbors(tiles)
corners = [tile for tile in tiles if sum(len(neighbor) for neighbor in tile.neighbors) == 2] # Corners have 2 neighbors
print(np.prod([corner.ID for corner in corners]))

# Day 20.2
with open("Day_20/pattern.txt", "r") as fin:
    monster_shape = [line for line in fin.read().replace(" ", ".").split("\n")]

board = build_image_board(tiles)
board, N_monsters = orient_to_monsters(board, monster_shape)
# In calculating the water roughness, we assumed that each sea monster was fully visible
print((board == "#").sum() - N_monsters * (np.array([list(line) for line in monster_shape]) == "#").sum())
