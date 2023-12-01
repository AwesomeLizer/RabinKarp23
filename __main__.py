from fasta import read_fasta
import sys
from random import randint


mod = 2**61 - 1
base = randint(1, mod)


def p_hash(text, base, mod):
    L_hash = [0]
    p = 1
    for sym in text:
        L_hash.append(((L_hash[-1] * base) % mod + ord(sym)) % mod)
        p = (p * base) % mod
    return (L_hash, p)



def get_loci(text, pattern, base, mod):

    pattern_hash, p = p_hash(pattern, base, mod)
    pattern_hash = pattern_hash[-1]
    text_hash = p_hash(text, base, mod)[0]
    pos = []
    for left_lim in range(len(text) - len(pattern) + 1):
        right_lim = left_lim + len(pattern)
        if pattern_hash == ((text_hash[right_lim] - (text_hash[left_lim] * p) % mod) % mod):
            pos.append(left_lim)

    return pos



if __name__ == '__main__':

    p_fa, t_fa = sys.argv[1:]

    pattern = read_fasta(p_fa)[1]
    text = read_fasta(t_fa)[1]

    res = get_loci(text, pattern, base, mod)
    print(*res)