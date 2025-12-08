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
input_1 = """987654321111111
811111111111119
234234234234278
818181911112111"""

sample_input = f"""{ input_1 }""".split('\n')

input_day = get_input("2025__3")

input_to_use = input_day
max_joltage = []
max_joltage2 = []


def get_max_voltage(input_number: int) -> int:
    str_number = str(input_number)
    l_n = len(str_number)
    d1 = max(list(str_number[0:-1]))
    d2 = max(list(str_number[str_number.index(d1)+1:]))
    return int(d1+d2)

# let's make it work with 2
def get_max_voltage_2(str_input_number: list[str], length_needed: int) -> int:
    # str_input_number = str(input_number)
    l_n = len(str_input_number)
    if length_needed == 1:
        return max(str_input_number)
    d1 = max(str_input_number[0:-length_needed+1])
    d2 = get_max_voltage_2(str_input_number[str_input_number.index(d1)+1:], length_needed -1)
    return d1+d2


ans1 = ans2 = 0
for item in input_to_use:
    max_joltage.append(get_max_voltage(item))
    max_joltage2.append(int(get_max_voltage_2(list(str(item)), 12)))
    
print('part 1:\t', sum(max_joltage))
print('part 2:\t', sum(max_joltage2))



# test_n = 234234234234278
# print('test')
# print(test_n, get_max_voltage(test_n))
