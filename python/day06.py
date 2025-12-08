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
input_1 = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

sample_input = f"""{ input_1 }""".split('\n')

input_day = get_input("2025__6")
input_to_use = input_day
# split ranges from ingredients

members = []
for item in input_to_use[:-1]:
    tmp = item.split(' ')
    tmp = list(map(lambda x: x.strip(), tmp))
    tmp = [int(i) for i in tmp  if i]
    members.append(tmp[:])# print(a)

operations = [i for i in list(map(lambda x: x.strip(), input_to_use[-1])) if i]

ans1 = 0
for group in range(0,len(operations)):
    if operations[group]  == '*':
        tmp = 1
        for item in members:
            tmp = tmp * item[group]
    elif operations[group]  == '+':
        tmp = 0
        for item in members:
            tmp = tmp + item[group]
    ans1 += tmp
print('part 1\t',ans1)
# part2
# ops symbol in first column of numbers

ops = list(input_to_use[-1])
# print(ops)
ops_map = dict()
for i in range(0,len(ops)):
    if ops[i].strip():
        ops_map[i] = {'op':ops[i]}
# print(ops_map)

ops_keys = list(ops_map.keys())
ops_keys.sort()
# print(ops_keys)
ops_keys.append(len(ops)+2)
# print(ops_keys)
for i in range(0, len(ops_keys)-1):
    ops_map[ops_keys[i]]['next'] = ops_keys[i+1]
# print(ops_map)
# print('assignment')
members2 = input_to_use[:-1]
for item in ops_map.keys():
    ops_map[item]['values'] = []
    for member in members2:
        ops_map[item]['values'].append(list(member[item:ops_map[item]['next']-1]))
    ops_map[item]['transposed'] =list(zip(*ops_map[item]['values'][::-1]))
    ops_map[item]['numbers'] = [ int(''.join(list(reversed(mb)))) for mb in ops_map[item]['transposed']]
# print(ops_map)
# print(ops_map[0]['values'])
# print(ops_map[0]['transposed'])
# print(ops_map[0]['numbers'])

ans2 = 0
for k,v in ops_map.items():
    if v['op'] == '*':
        tmp = 1
        for item in v['numbers']:
            tmp = tmp * item
    elif v['op']  == '+':
        tmp = 0
        for item in v['numbers']:
            tmp = tmp + item
    ans2 += tmp
print('part 2:\t', ans2)