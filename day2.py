def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split()
            data.append((line[0], int(line[1])))
    return data

data = get_data("day2.txt")

aim = 0
depth = 0
forward = 0
for direct, n in data:
    if direct == "forward":
        forward += n
        depth += n * aim
    elif direct == "up":
        aim -= n
    elif direct == "down":
        aim += n

print(forward)
print(depth)
print(depth*forward)

