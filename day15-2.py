from heapq import heappop, heappush

def scout_neighs(x, y, xymap, maxx, maxy, heap):
    # print(self.neighs)
    data = xymap[(x, y)]
    # print("XXX", x, y, data)

    if x > 0:
        neigh_data = xymap[(x - 1, y)]
        if neigh_data["visited"] == False:
            # print(data["total_danger"] + neigh_data["val"], neigh_data["total_danger"])
            neigh_data["total_danger"] = min(data["total_danger"] + neigh_data["val"], neigh_data["total_danger"])
            if neigh_data["queued"] == False:
                heappush(heap, (neigh_data["total_danger"], (x - 1, y)))
                neigh_data["queued"] = True
    if x < maxx:
        neigh_data = xymap[(x + 1, y)]
        if neigh_data["visited"] == False:
            # print(data["total_danger"] + neigh_data["val"], neigh_data["total_danger"])
            neigh_data["total_danger"] = min(data["total_danger"] + neigh_data["val"], neigh_data["total_danger"])
            if neigh_data["queued"] == False:
                heappush(heap, (neigh_data["total_danger"], (x + 1, y)))
                neigh_data["queued"] = True
    if y > 0:
        neigh_data = xymap[(x, y - 1)]
        if neigh_data["visited"] == False:
            # print(data["total_danger"] + neigh_data["val"], neigh_data["total_danger"])
            neigh_data["total_danger"] = min(data["total_danger"] + neigh_data["val"], neigh_data["total_danger"])
            if neigh_data["queued"] == False:
                heappush(heap, (neigh_data["total_danger"], (x , y - 1)))
                neigh_data["queued"] = True
    if y < maxy:
        neigh_data = xymap[(x, y + 1)]
        if neigh_data["visited"] == False:
            # print(data["total_danger"] + neigh_data["val"], neigh_data["total_danger"])
            neigh_data["total_danger"] = min(data["total_danger"] + neigh_data["val"], neigh_data["total_danger"])
            if neigh_data["queued"] == False:
                heappush(heap, (neigh_data["total_danger"], (x , y + 1)))
                neigh_data["queued"] = True

    data["visited"] = True

def get_pos_val(xymap, x, y, origxlen, origylen):
    #work out how many cells down and accros it is
    xcell = x // origxlen
    ycell = y // origylen
    adding = xcell +  ycell

    # get x and y mapped to small area
    new_x = x % origxlen
    new_y = y % origylen

    # base val 
    base_val = xymap[(new_x, new_y)]
    add_val = base_val + adding

    #loop back around
    if add_val > 9:
        add_val = (add_val % 10) + 1
    return add_val


def get_data(filename):
   
    with open(filename, 'r') as f:
        mapxy = {}
        for y, line in enumerate(f):
            line = [int(i) for i in list(line.strip())]
            for x, score in enumerate(line):
                mapxy[((x, y))] = score
    return mapxy, x, y


mapxy, maxx, maxy = get_data("day15.txt")
NUM = 5

print("####", maxx, maxy)

maxbigx = NUM * (maxx + 1) - 1
maxbigy = NUM * (maxy + 1) - 1

big_xymap = {}
for y in range(maxbigy + 1):
    for x in range(maxbigx + 1):
        val = get_pos_val(mapxy, x, y, maxx+1, maxy+1)
        big_xymap[(x, y)] = {"x": x, "y": y, "val": val, "visited": False, "total_danger": 10000000, "queued": False}
        # print(big_xymap[(x, y)]["val"], end="")
        
    # print()
        # Node(x, y, get_pos_val(mapxy, x, y, maxx+1, maxy+1))

# for node in nodes.values():
#     node.add_neighs(nodes, x, y)


start = (0, 0)
start_data = big_xymap[start]
start_data["total_danger"] = 0
end = (maxbigx, maxbigy)
end_data = big_xymap[(end)]
heap = []

print(big_xymap[(0, 0)])

current_node = start
while not end_data["visited"]:
    currentx, currenty = current_node
    scout_neighs(currentx, currenty, big_xymap, maxbigx, maxbigy, heap)
    # print(nodes)
    # print(len(heap))

    if heap:
        val, current_node = heappop(heap)


    # if len([1 for data in big_xymap.values() if not data["visited"]]) > 0:
    #     current_node = min([n for n in big_xymap.items() if not n[1]["visited"]], key=lambda x: x[1]["total_danger"])[0]

print(x, y)
# print([node.danger_total for node in nodes.values()])
# print([data["total_danger"] for data in big_xymap.values() ])
print(end_data)

print(len([d for d in big_xymap.items() if d[1]["total_danger"]<1000000]))