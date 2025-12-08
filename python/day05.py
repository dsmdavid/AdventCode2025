from copy import deepcopy
from multiprocessing import process
from re import L
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
input_1 = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

sample_input = f"""{ input_1 }""".split('\n')

input_day = get_input("2025__5")
input_to_use = input_day
# split ranges from ingredients

def process_range(range_str: str) -> tuple[int,int]:
    return tuple(map(int,range_str.split('-')))
    
def process_input(raw_input: list[str]) -> (list, list):
    split_point = raw_input.index('')
    ranges = list(map(process_range, raw_input[0:split_point]))
    ingredients = list(map(int,raw_input[split_point+1:]))
    # print(raw_input, split_point, ranges, fresh)
    return ranges, ingredients


fresh, ingredients = process_input(input_to_use)
ans1 = ans2 = 0
fresh_ingredients = []
for i in ingredients:
    for k in fresh:
        if i >= k[0] and i <= k[1]:
            fresh_ingredients.append(i)
            break 
ans1 = len(fresh_ingredients)
print('part 1:\t', ans1)

def overlap_two_lists(list_a, list_b) -> list[tuple]:
    min_a = min(list_a)
    max_a = max(list_a)
    min_b = min(list_b)
    max_b = max(list_b)
    if (min_a <= min_b and max_a >= min_b) or (min_b <= min_a and max_b >= min_a):  
        min_c = min(min_a, min_b)
        max_c = max(max_a, max_b)
        return [(min_c, max_c)]
    else:
        return [(min_a,max_a),(min_b,max_b)]

# part 2: consolidate

def consolidate(list_of_tuples: list[tuple]) -> (list[tuple]):
    not_overlapping = []
    static = deepcopy(list_of_tuples)
    changes = True
    while changes:
        tmp = set()
        changes = False
        for i in static:
            # print(ct, 1, i)
            flag_i = True
            for k in static:
                # print(ct,2, i,k)
                if i != k:
                    check = overlap_two_lists(i,k)
                    # print(ct,3,check, set(check))
                    if i not in check:
                        flag_i = False 
                        changes = True
                        tmp = tmp.union(check)
                        # print(ct,4,tmp)

            if flag_i:
                not_overlapping.append(i)
        static = list(deepcopy(tmp))
    return set(not_overlapping)

consolidated = consolidate(fresh)
ans2 = 0
for item in consolidated:
    ans2 += 1 + item[1] - item[0]

print('part 2:\t', ans2, len(consolidated))
