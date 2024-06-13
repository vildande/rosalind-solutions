# dna sequence given
dna = "AAAACCCGGT"

# reverse dna
dna_reversed = dna[::-1]

# find complement
complement_map = str.maketrans('AGCT', 'TCGA') # translation table
dna_reversed_compl = dna_reversed.translate(complement_map)


print(dna_reversed_compl)