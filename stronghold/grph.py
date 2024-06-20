"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

from Bio import SeqIO

def overlap_graph_3(records):
    sequence_items = [(r.id, r.seq) for r in records]
    k = 3
    edges = []

    # if suffix of s is equal to suffix of t, add edge (s, t)
    for s_label, s_seq in sequence_items:
        s_suffix = s_seq[-k:]
        for t_label, t_seq in sequence_items:
            if s_label != t_label:
                t_prefix = t_seq[:k]
                if s_suffix == t_prefix:
                    edges.append((s_label, t_label))
    return edges

def print_edges(edges):
    for e in edges:
        print(f"{e[0]} {e[1]}")


if __name__ == '__main__':
    # reading FASTA file
    filename = "../data/grph.fasta"
    records = SeqIO.parse(filename, "fasta")
    adj_list = overlap_graph_3(records)
    print_edges(adj_list)
