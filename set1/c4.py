from typing import Tuple
from .c3 import brute_single_char_xor

with open("set1/4.txt", "r") as f:
    lines = [bytes.fromhex(line) for line in f.readlines()]

best: Tuple[int, str, chr] = (0, "", '')

for line in lines:
    result = brute_single_char_xor(line)
    if result[0] > best[0]:
        best = result

print(best[1])
