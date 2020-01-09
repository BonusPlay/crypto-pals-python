from typing import List

from bitarray import bitarray
from base64 import b64decode
from .c3 import brute_single_char_xor
from .c5 import xor_repeating


def hammering_distance(a: bytes, b: bytes) -> int:
    bits_a = bitarray()
    bits_a.frombytes(a)

    bits_b = bitarray()
    bits_b.frombytes(b)

    return sum([bit_a ^ bit_b for bit_a, bit_b in zip(bits_a, bits_b)])


assert(hammering_distance(b"this is a test", b"wokka wokka!!!") == 37)


def find_keysize(data: bytes) -> int:
    distances_array = [(hammering_distance(data[:length], data[length: 2 * length]) / length, length) for length in range(2, 25)]
    return min(distances_array, key=lambda item: item[0])[1]


if __name__ == "__main__":
    with open("set1/6.txt", "r") as f:
        content: bytes = b64decode(f.read())

    keysize = find_keysize(content)
    print(f"Keysize: {keysize}")

    key = ""

    for i in range(1, keysize + 1):
        part = content[i::keysize]
        result = brute_single_char_xor(part)
        key += result[2]

    print(xor_repeating(content, key.encode("ascii")).decode("ascii"))
