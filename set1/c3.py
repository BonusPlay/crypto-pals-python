from typing import Dict, Tuple

weight: Dict[str, float] = {
    'A': 0.0651738,
    'B': 0.0124248,
    'C': 0.0217339,
    'D': 0.0349835,
    'E': 0.1041442,
    'F': 0.0197881,
    'G': 0.0158610,
    'H': 0.0492888,
    'I': 0.0558094,
    'J': 0.0009033,
    'K': 0.0050529,
    'L': 0.0331490,
    'M': 0.0202124,
    'N': 0.0564513,
    'O': 0.0596302,
    'P': 0.0137645,
    'Q': 0.0008606,
    'R': 0.0497563,
    'S': 0.0515760,
    'T': 0.0729357,
    'U': 0.0225134,
    'V': 0.0082903,
    'W': 0.0171272,
    'X': 0.0013692,
    'Y': 0.0145984,
    'Z': 0.0007836,
    ' ': 0.1918182
}


def rate(a: str) -> int:
    return sum([weight.get(b.capitalize(), 0) for b in a])


def brute_single_char_xor(a: bytes) -> Tuple[int, str, chr]:
    best: Tuple[int, str, chr] = (0, "", '')

    for i in range(255):
        try:
            result = bytes([b ^ i for b in a]).decode("ascii")
        except:
            continue
        total = rate(result)
        if total > best[0]:
            best = (total, result, chr(i))

    return best


# print(brute_single_char_xor(bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))[1])
