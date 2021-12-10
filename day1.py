def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(int(line.strip()))
    return data

import os
print(os.getcwd())

data = get_data("day1a.txt")

count = 0
for i in range(3, len(data)):
    if sum(data[i - 4: i - 1]) < sum(data[i - 3: i]):
        count += 1

print(count)





