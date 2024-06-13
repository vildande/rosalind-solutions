# used biopython package
from Bio import SeqIO 
from Bio.SeqUtils import gc_fraction

# FASTA file where I put the dataset
filename = "../data/gc.fasta"

# parse the FASTA file
records = SeqIO.parse(filename, "fasta")

# find the record with largest gc_content
max_record = max(records, key=lambda record: gc_fraction(record.seq))


# print name of the sequence and its gc_content (in percent rounded to 6 digits)
print(max_record.id)
print('{0:.6f}'.format(100 * gc_fraction(max_record.seq)))
