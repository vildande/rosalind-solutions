# file with the dataset
filename = '../data/hamm.txt'

# list of DNA strings
dnas = []

# read the first two lines of the file
with open(filename, 'r') as d:
    dnas = [d.readline().strip() for _ in range(2)]

# count the differences in two DNA strings
diff_count = sum(1 for n1, n2 in zip(dnas[0], dnas[1]) if n1 != n2)


print(diff_count)