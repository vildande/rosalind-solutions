
def expected_dominant(couples):
    # genotypes for each couple:
    # 1. AA-AA
    # 2. AA-Aa
    # 3. AA-aa
    # 4. Aa-Aa
    # 5. Aa-aa
    # 6. aa-aa

    # the probabilities for each genotype pairing 
    probabilities = [1, 1, 1, 0.75, 0.5, 0]

    expected_offspring = 0 
    
    # assuming every couple produces exactly two offspring
    for i in range(6):
        expected_offspring += couples[i] * probabilities[i] * 2
    
    return expected_offspring


if __name__ == "__main__":
    # file with the dataset
    filename = '../data/iev.txt'

    # number of couples corresponding to each genotype pairing
    couples = []

    # read the first two lines of the file
    with open(filename, 'r') as d:
        couples = list(map(int, d.readline().strip().split()))
    
    
    print(expected_dominant(couples))