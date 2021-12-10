class Spot():
    def __init__(self, x, y, num):
        self.num = int(num)
        self.x = x
        self.y = y
        self.neighs = None

    def set_neighs(self, mapxy, maxx, maxy):
        neigh_nodes = []
        if self.x - 1 >= 0 and self.x - 1 <= maxx:
            neigh_nodes.append(mapxy[(self.x - 1, self.y)])
        if self.x + 1 >= 0 and self.x + 1 <= maxx:
            neigh_nodes.append(mapxy[(self.x + 1, self.y)])
        if self.y - 1 >= 0 and self.y - 1 <= maxy:
            neigh_nodes.append(mapxy[(self.x, self.y - 1)])
        if self.y + 1 >= 0 and self.y + 1 <= maxy:
            neigh_nodes.append(mapxy[(self.x, self.y + 1)])
        self.neighs = neigh_nodes

    def get_basin_neighs(self, visted_spots=set()):
        # add all neighs that arent too big to the basin and coord list. 
        # for each of the neighs traverse to find their basins, returning basin and updated coord list that can be used by the next branch
        basin = [self] 
        visted_spots.add(self)
        print(self.x, self.y)
        for n in self.neighs:
            if n.num < 9 and n not in visted_spots:
                n_basin, visted_spots = n.get_basin_neighs(visted_spots=visted_spots)
                print("\n########")
                print([b.num for b in basin], [b.num for b in n_basin])
                basin = basin + n_basin
                print([b.num for b in basin])
        return basin, visted_spots



def get_data(filename):
    # from collections import defaultdict
    # mapxy = defaultdict(lambda: Spot(None, None, 1000000))
    mapxy = {}
    with open(filename, 'r') as f:
        for y, line in enumerate(f):
            line = list(line.strip())
            for x, num in enumerate(line):
                mapxy[(x, y)] = Spot(x, y, num)

    for spot in mapxy.values():
        spot.set_neighs(mapxy, x, y)
    return mapxy, x, y


# def get_neigh_nums(mapxy, x, y):
#     neigh_nums = []
#     neigh_nums.append(mapxy[(x - 1, y)])
#     neigh_nums.append(mapxy[(x + 1, y)])
#     neigh_nums.append(mapxy[(x, y - 1)])
#     neigh_nums.append(mapxy[(x, y + 1)])
#     return neigh_nums
    

mapxy, maxx, maxy = get_data("day9.txt")

print(mapxy.keys())

mins = []

for y in range(maxy + 1):
    for x in range(maxx + 1):
        spot = mapxy[(x, y)]
        neigh_nums = [n.num for n in spot.neighs]
        if all([spot.num < neigh for neigh in neigh_nums]):
            mins.append(spot)
print("###", [m.num for m in mins])

# print(mins)
# dang = sum([m + 1 for m in mins])
# print(dang)

basin_size = {}
for min in mins:
    print("%%%%%%%%%%%%")
    basin_size[min] = len(min.get_basin_neighs()[0])

# print(basin_size)

for k,v in basin_size.items():
    print(k.num, k.x, k.y, v)

sizes = sorted(list(basin_size.values()), reverse=True)
from math import prod
print(prod(sizes[0:3]))