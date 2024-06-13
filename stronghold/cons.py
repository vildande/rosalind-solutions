from Bio import SeqIO 
from collections import Counter

def get_profile_matrix(dna_strings):
    profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    
    # going through each column of the dna strings
    for column in zip(*dna_strings):
        # count occurrences of each base in the column
        column_counts = Counter(column)  

        # add the counts for each base to the matrix
        for base in 'ACGT':
            profile_matrix[base].append(column_counts[base])
    
    return profile_matrix

def get_consensus_sequence(profile_matrix):
    consensus = ''
    for i in range(len(profile_matrix['A'])):
        # find the base with the max count at the current position
        max_base = max('ACGT', key=lambda base: profile_matrix[base][i])
        
        # add that base to the consensus
        consensus += max_base
    return consensus

if __name__ == '__main__':
    # reading FASTA file
    filename = "../data/cons.fasta"
    records = SeqIO.parse(filename, "fasta")
    dna_seqs = [rec.seq for rec in records]
    
    matrix = get_profile_matrix(dna_seqs)
    consensus = get_consensus_sequence(matrix)


    print(consensus)
    for key, values in matrix.items():
        print(f"{key}: {' '.join(map(str, values))}")
