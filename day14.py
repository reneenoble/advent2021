from typing import Counter

def get_data(filename):
    rules = {}
    sect2_found = False
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                start = line.strip()
            elif i > 1:
                line = line.strip().split(" -> ")
                rules[line[0]] = line[1]

    return start, rules


start, rules = get_data("day14.txt")

pair_count = {pair: 0 for pair in rules.keys()}
for j in range(len(start) - 1):
    pair = start[j] + start[j+1]
    pair_count[pair] += 1


for i in range(40):
    new_pair_count = {pair: 0 for pair in rules.keys()}
    for pair, count in pair_count.items():
        new_pat_1 = rules[pair]
        new_pat_2 = rules[pair]
        new_pair_count[pair[0] + new_pat_1] += count
        new_pair_count[new_pat_2 + pair[1]] += count
    pair_count = new_pair_count
print(pair_count)

from collections import defaultdict
letters_count = defaultdict(int)
for pair, count in pair_count.items():
    pair1, pair2 = pair
    letters_count[pair1] += count
    letters_count[pair2] += count

first = start[0]
last = start[-1]
letters_count[first] += 1
letters_count[last] += 1

letters_count = {k: v/2 for k, v in letters_count.items()}
maxv = max(letters_count.values())
minv = min(letters_count.values())

print(maxv-minv)


# Part 1
# for i in range(40):
#     print(i)
#     new_poly = ""
#     for j in range(len(start) - 1):
#         # print(j,start[j] + start[j+1] )
#         pair = start[j] + start[j+1]
#         new_poly = new_poly + pair[0] + rules[pair]
#     new_poly = new_poly + pair[1]
    
#     # print(new_poly)
    
#     start = new_poly
#     count = Counter(start)
#     # print(i, count)

# maxv = max(count.values())
# minv = min(count.values())
# print(maxv - minv)
