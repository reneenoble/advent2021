from collections import defaultdict
import math

def get_data(filename):
    from collections import defaultdict
    coords = defaultdict(bool)
    folds = []
    sect2_found = False
    with open(filename, 'r') as f:
        for line in f:
            if line == "\n":
                sect2_found = True
            elif not sect2_found:
                line = [int(coord) for coord in line.strip().split(",")]
                coords[tuple(line)] = True
            else:
                fold = line.split("=")
                axis = fold[0][-1]
                position = fold[1]
                folds.append((axis, int(position)))
    return coords, folds

def print_plane(plane, maxx, maxy):
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if plane[(x, y)]:
                symb = "#"
            else:
                symb = "."
            print(symb, end="")
        print()
    print("\n\n")

plane, folds = get_data("day13.txt")

# def add_planes(a, b, axis):


# def fold(coords, axis, position):
#     if axis == x:
#         coord = 0
#     else:
#         coord = 1
    
#     for x, y in coords.keys():

maxx = max([x for x, y in plane.keys()])
maxy = max([y for x, y in plane.keys()])
print(maxx, maxy)

# print_plane(plane, maxx, maxy)

for fold in folds:


    # print(plane)
    # maxx = max([x for x, y in plane.keys()])
    # maxy = max([y for x, y in plane.keys()])

    # plane = []
    print(fold[1], fold[0])
    new_plane = defaultdict(bool)
    if fold[0] == "x":
        overlap_start = (maxx - (2*(maxx - fold[1]) + 1)) + 1
        for y in range(maxy + 1):
            for x in range(fold[1]):
                new_plane[(x, y)] = plane[(x, y)] or plane[((fold[1]*2) - x, y)]


                # if x >= overlap_start:
                #     new_plane[(x, y)] = plane[(x, y)] or plane[(maxx - x, y)]
                # else:
                #    new_plane[(x, y)] = plane[(x, y)] 
        maxx = fold[1] - 1


    elif fold[0] == "y":
        # overlap_w = maxy - fold[1]
        overlap_start = (maxy - (2*(maxy - fold[1]) + 1)) + 1
        for x in range(maxx + 1):
            for y in range(fold[1]):
                if y >= overlap_start:
                    new_plane[(x, y)] = plane[(x, y)] or plane[(x, (fold[1]*2) - y)]
                else:
                   new_plane[(x, y)] = plane[(x, y)] 
        maxy = fold[1] - 1

    

    # print(new_plane)
    # print(len([1 for v in new_plane.values() if v]))

    plane = new_plane
    print_plane(plane, maxx, maxy)
    # break



print(len([1 for v in new_plane.values() if v]))

# axis, position = folds[0]
