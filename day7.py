def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        data = [int(i) for i in f.read().strip().split(",")]
    return data


def fuel_cost(dist):
    return sum([i for i in range(1, dist + 1)])

pos = get_data("day7.txt")
print(pos)

from statistics import median

ave = sum(pos)/len(pos)
med = median(pos)
print("Data", ave, med)

import math
# lower = math.floor(ave)
# upper = math.ceil(ave)

m_diffs = [fuel_cost(abs(i - math.floor(ave))) for i in pos] 
print(m_diffs)
print(sum(m_diffs))

# u_diffs = [abs(i - upper) for i in pos]
# print(sum(u_diffs))

# med 98685593
# ave 90041060
# fav 90040997