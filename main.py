from util import hash, get_word_combs
from tqdm import tqdm
from math import ceil
from random import sample

# get words from file
with open('wordlist.txt', 'r') as f:
    words = f.read().splitlines()

# shuffle words
wordlist = sample(words, len(words))

# calculate n of iterations
n_bits = 45
k = 10
total = ceil(1.177 * 2 ** (ceil(n_bits / 2)))
print("Words to be checked: ", total)

pbar = tqdm(total=total)
lookup = dict()
done = False
n = 0

for x in wordlist:
    if done:
        break
    # get word combinations
    for p in get_word_combs(x):
        n += 1
        pbar.update(1)
        if n > total:
            done = True
            break

        # hash
        h = hash(p.encode('UTF-8'), n_bits, k)

        if h in lookup:
            if p not in lookup.values():
                pbar.close()
                print("Done")
                print("s1 =", p)
                print("s1 hash = ", hash(p.encode('UTF-8'), n_bits, k))
                print("s2 =", lookup[h])
                print("s2 hash = ", hash(lookup[h].encode('UTF-8'), n_bits, k))
                done = True
                break
            else:
                print("Duplicate")
                break
        else:
            lookup[h] = p

pbar.close()
# s1 d54e9d8e75d0ec15
# s1 hash =  1110110100100000111001001010101001100100010010
# s2 46b4808efdcab54a
# s2 hash =  1110110100100000111001001010101001100100010010

# s1 9429fe542a7bde6e
# s1 hash =  1000100011101100101011100001110101100111011000
# s2 f6a077e6b0467d74
# s2 hash =  1000100011101100101011100001110101100111011000

# s1 = ARCHcoNFRatErNItIeS
# s1 hash =  1011101110010100100100011010011010000110110110
# s2 = WeIERStRAsSIAn
# s2 hash =  1011101110010100100100011010011010000110110110

# s1 = NOnFuGitiVENEss
# s1 hash =  1001001111010100101010111111100101000010111111
# s2 = ChlamydobAcTEriaceAE
# s2 hash =  1001001111010100101010111111100101000010111111

# s1 SpErMaTORRHOea
# s1 hash =  1000010011100101101110111000100100011100111111
# s2 sEMiPHILoSoPHiCAlLy
# s2 hash =  1000010011100101101110111000100100011100111111

# s1 = crYSTAlLOChemIStRY
# s1 hash =  1100011110011101111000111110001101101001100010
# s2 = semIpHilosOphIcaLlY
# s2 hash =  1100011110011101111000111110001101101001100010
