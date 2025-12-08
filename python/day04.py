from copy import deepcopy
import sys
import os
from typing import List, Tuple
from collections import defaultdict, deque
from math import inf, floor
import functools

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)
from utils.log import MyLogger
from utils.tools import get_input

logger = MyLogger(log_file="aoc2025.log", log_path="logs", name=__name__)
input_1 = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

sample_input = f"""{ input_1 }""".split('\n')

input_day = get_input("2025__4")
input_to_use = input_day

GRID = defaultdict(lambda: '.')

accessible = []

def get_neighbours(coords: tuple[int,int], grid) -> int:
    cnt = 0
    if grid[coords] == '@':
        for i in range (-1,2):
            for j in range(-1,2):
                if not (i==0 and j == 0):
                    if grid[(coords[0]+i,coords[1]+j)] == '@':
                        cnt +=1
        return cnt
    return 4

def print_grid(grid):
    row_ = max([coord[0] for coord in grid.keys()])
    col_ = max([coord[1] for coord in grid.keys()])
    min_row_ = min([coord[0] for coord in grid.keys()])
    min_col_ = min([coord[1] for coord in grid.keys()])
    print(min_row_, row_,min_col_, col_)
    tmp = ''
    for i in range(min_row_, row_ +1):
        for j in range(min_col_, col_ + 1):
            tmp += grid[i,j]
        tmp += '\n'
    print(tmp)

ans1 = ans2 = 0
# populate GRID

for row in range(0, len(input_to_use)):
    for col in range(0, len(input_to_use[0])):
        # print(row, col, input_to_use[row][col])
        GRID[(row,col)] = input_to_use[row][col]
ACTUAL_GRID = deepcopy(GRID)
# count neighbours
for coord in ACTUAL_GRID.keys():
    if get_neighbours(coord, GRID) < 4:
        accessible.append(coord)

print('part 1:\t', len(accessible))

# part_2
# reset inputs
removed = []
accessible = []
flag_continue = True
while flag_continue:
    GRID = deepcopy(ACTUAL_GRID)
    for coord in ACTUAL_GRID.keys():
        if get_neighbours(coord, GRID) < 4:
            accessible.append(coord)
    if len(accessible) > 0:
        for item in accessible:
            ACTUAL_GRID[item] = 'x'
            removed.append(item)
        accessible = []
    else:
        flag_continue = False 
print('part_2:\t',len(removed))