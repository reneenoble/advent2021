from collections import defaultdict

def get_data(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            point_pair = [[int(i) for i in p.split(",")] for p in line.strip().split(" -> ")]
            print(point_pair)
            lines.append(point_pair)
    return lines


lines = get_data("day5.txt")

map_sum = defaultdict(int)
for p1, p2 in lines:
    if p1[0] == p2[0]:
        x = p1[0]
        miny = (min(p1[1], p2[1]))
        maxy = (max(p1[1], p2[1]))
        for y in range(miny, maxy+ 1):
            map_sum[(x, y)] += 1
    
    elif p1[1] == p2[1]:
        y = p1[1]
        minx = (min(p1[0], p2[0]))
        maxx = (max(p1[0], p2[0]))
        for x in range(minx, maxx+ 1):
            map_sum[(x, y)] += 1

    else:
        start = (min(p1, p2))
        end = (max(p1, p2))
        minx = start[0]
        maxx = end[0]
        y = start[1]
        if y == min(p1[1], p2[1]):
            yop = 1
        else:
            yop = -1

        for x in range(minx, maxx+ 1):
            map_sum[(x, y)] += 1
            y += yop

for y in range(10):
    for x in range(10):
        print(map_sum[(x,y)], end="")
    print()

print(map_sum)
print(len([i for i in map_sum.values() if i >= 2]))