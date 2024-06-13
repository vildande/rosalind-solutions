# k - number of homozygous dominant
# m - number of heterozygous
# n - number of homozygous recessive

k, m, n = 2, 2, 2


# To get dominant phenotype, there must be at least 1 dominant factor.
# Five possible matings that can lead to dominant phenotype:
# 1) k + k
# 2) m + m
# 3) k + m
# 4) k + n
# 5) m + n

# in type 1, there's 100% chance of getting domninant phenotype (AA, AA, AA, AA)
# in type 2, there's 75% chance of getting domninant phenotype  (AA, Aa, aA, aa) 
# in type 3, there's 100% chance of getting domninant phenotype  (AA, Aa, AA, aA)
# in type 4, there's 100% chance of getting domninant phenotype  (Aa, Aa, Aa, Aa)
# in type 5, there's 50% chance of getting domninant phenotype  (Aa, Aa, aa, aa)

# doing some math...
N = k + m + n
T1 = (k/N) * ((k-1)/(N-1))
T2 = (m/N) * ((m-1)/(N-1))
T3 = (k/N) * (m/(N-1)) + (m/N) * (k/(N-1))
T4 = (k/N) * (n/(N-1)) + (n/N) * (k/(N-1))
T5 = (m/N) * (n/(N-1)) + (n/N) * (m/(N-1))
phendom = 1.0 * T1 + 0.75 * T2 + 1.0 * T3 + 1.0 * T4 + 0.5 * T5


print(f"{phendom:.5f}")
