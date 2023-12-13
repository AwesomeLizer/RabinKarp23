from fasta import read_fasta
from newkarp import rabin_karp
import sys




if __name__ == '__main__':

    p_fa, t_fa = sys.argv[1:]

    pattern = read_fasta(p_fa)[1]
    text = read_fasta(t_fa)[1]

    res = rabin_karp(text, pattern)
    print(*res)