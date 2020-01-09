from itertools import cycle


def xor_repeating(text: bytes, key: bytes) -> bytes:
    assert(len(text) > len(key))
    return bytes([a ^ b for a, b in zip(text, cycle(key))])


assert(xor_repeating("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode("utf-8"), "ICE".encode("utf-8")) == bytes.fromhex("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"))