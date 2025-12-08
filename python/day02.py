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
input_1 = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

sample_input = f"""{ input_1 }"""

input_day = get_input("2025__2")[0]
print(input_day)

input_to_use = input_day
input_ranges = input_to_use.split(',')
invalid_nunmbers = []
invalid_nunmbers2 = []
def is_repeated(input_number: int) -> bool:
    str_number = str(input_number)

    l_n = len(str_number)
    if l_n % 2 != 0:
        return False 
    else:
        a = str_number[0:int(l_n/2)]
        b = str_number[int(l_n/2):]
        return a == b

def is_invalid2(input_number:int) -> bool:
    str_number = str(input_number)
    l_n = len(str_number)

    for i in range(1,l_n//2+1):
        if l_n % i == 0:
            a = str_number[0:i]
            test = a*int(l_n / i)
            # print(test, str_number, test == str_number)
            if test == str_number:
                return True

    return False

ans1 = ans2 = 0

for test_range in input_ranges:
    start = int(test_range.split('-')[0])
    end = int(test_range.split('-')[1])
    for n in range(start, end+1,1):
        if is_repeated(n):
            ans1 += 1
            invalid_nunmbers.append(n)
        if is_invalid2(n):
            ans2 += 1
            invalid_nunmbers2.append(n)

    
print(ans1, '\tinvalid numbers, adding up to:', sum(invalid_nunmbers))
print(ans2, '\tinvalid numbers_2, adding up to:', sum(invalid_nunmbers2))

# print('test')
# print(1188511885, is_repeated(1188511885))
# print(1188511885, is_invalid2(1188511885))