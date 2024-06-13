# DNA string (given)
dna = "GATGGAACTTGACTACGTAAATT"

# transcribe DNA to RNA
transcr_map = str.maketrans('AGCT', 'AGCU') # translation table
rna = dna.translate(transcr_map)


print(rna)