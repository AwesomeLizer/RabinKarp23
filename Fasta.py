def read_fasta(path):
    with open(path) as f:
        lines = f.readlines()
        sq_name = lines[0]
        sq = ''.join(lines[1:])
        return sq_name, sq