'''
Given: Two DNA strings s and t
Return: All locations of t as a substring of s.
'''

def find_subs(source, pattern):
    # find indexes where patterm is found in source
        # adust to 1-based indexing
        # go everywhere where the pattern can be possibly found
        # if pattern found, add index
    return [
        i+1 \
        for i in range(len(source) - len(pattern) + 1) \
        if source[i:i + len(pattern)] == pattern
    ]



if __name__ == "__main__":
    # file with the dataset
    filename = '../data/subs.txt'
    # list of DNA strings
    dnas = []
    # read the first two lines of the file
    with open(filename, 'r') as d:
        dnas = [d.readline().strip() for _ in range(2)]
    
    subs = find_subs(dnas[0], dnas[1])

    print(*subs)