def read_fasta(path):
    with open(path) as f:
        sq_name = f.readline()
        sq = ''

        for line in f:
            sq += line[:-1]

        return sq_name, sq