"""
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

def mortal_rabbits(months, ttl):
    # list of rabbit pairs for each month (1st month at index 0, 2nd month at index 1, and so on)
    rabbits = [0] * months

    # initial pair of rabbits
    rabbits[0] = 1
    rabbits[1] = 1

    # simulating population dynamics for each month
    for i in range(2, months):
        # rabbits = kids + adults
        if i < ttl:
            rabbits[i] = rabbits[i-1] + rabbits[i-2]
        
        # rabbits = kids + adults - dead (first pair)   :: first pair was born exactly ttl months ago
        elif i == ttl:
            rabbits[i] = rabbits[i-1] + rabbits[i-2] - rabbits[i - ttl]
        
        # rabbits = kids + adults - dead (other pairs)  :: all other pairs were born ttl + 1 months ago
        elif i > ttl:
            rabbits[i] = rabbits[i-1] + rabbits[i-2] - rabbits[i - ttl - 1]

    return rabbits[months - 1]


if __name__ == '__main__':
    #reading input
    filename = "../data/fibd.txt" 
    months = 0 # how much months past
    ttl =  0 # time to live for each rabbit
    with open(filename, 'r') as file:
        months, ttl = map(int, file.readline().strip().split())

    print(mortal_rabbits(months, ttl))