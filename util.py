from bitstring import BitArray
import whirlpool


def hash(x: str, trim=45, start=10):
    wp = whirlpool.new(x)
    hashed = wp.digest()
    bitstr = BitArray(hashed).bin[start:start+trim+1]
    return bitstr


def get_word_combs(word: str):
    w = word.lower()
    l = len(w)
    for i in range(2 ** l):
        bit_mask = BitArray(uint=i, length=l).bin
        s = "".join(char.upper() if bit == "1" else char.lower()
                    for char, bit in zip(w, bit_mask))
        yield s
