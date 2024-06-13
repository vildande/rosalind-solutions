# n month, k offsping from each pair
n, k = 5, 3 

# 1st month (only 1 pair which is not in reproductive-age)
pairs_mature = 0 # reproductive-age pairs of rabbits
pairs_all = 1 # all pairs of rabbits (adults and kids)

# going from the 1st month to the nth
for _ in range(1, n):
    # updating the variables: 
    # 1) next number of pairs = all adults pairs from the past + their offspring
    # 2) all the pairs from the past are now mature 
    pairs_all, pairs_mature = pairs_all + pairs_mature * k, pairs_all


print(pairs_all)
