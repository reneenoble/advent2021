def get_data(filename):
    with open(filename, 'r') as f:
        mapxy = {}
        for y, line in enumerate(f):
            line = [int(i) for i in list(line.strip())]
            for x, score in enumerate(line):
                mapxy[((x, y))] = score
        
    return mapxy, x, y

def get_pos_val(xymap, x, y, origxlen, origylen):
    # print("inputs", x, y, origxlen, origylen)

    #work out how many cells down and accros it is
    xcell = x // origxlen
    ycell = y // origylen
    adding = xcell +  ycell
    # print("cells, adder", xcell, ycell, adding)

    # get x and y mapped to small area
    new_x = x % origxlen
    new_y = y % origylen
    # print("newx, newy", new_x, new_y)

    # base val 
    base_val = xymap[(new_x, new_y)]
    add_val = base_val + adding
    # print(base_val, add_val)

    #loop back around
    if add_val > 9:
        add_val = (add_val % 10) + 1
    # print(add_val)
    return add_val
    

mapxy, maxx, maxy = get_data("day15demo.txt")

score_to_pos  = {}
dirs  = {}

# add (0, 0)
score_to_pos[(0, 0)] = 0

dirs[(0, 0)] = "X"
print(get_pos_val(mapxy, 0, 0, maxx+1, maxy+1), end="")

NUM = 5
# add top row
for x in range(1, NUM * (maxx +1)):
    this_spot = get_pos_val(mapxy, x, 0, maxx+1, maxy+1)
    score_to_pos[(x, 0)] = score_to_pos[(x - 1, 0)] + this_spot
    dirs[(x, 0)] = "<"
    print(this_spot, end="")
print()

# add left col
for y in range(1, NUM * (maxy +1)):
    this_spot = get_pos_val(mapxy, 0, y, maxx+1, maxy+1)
    score_to_pos[(0, y)] = score_to_pos[(0, y - 1)] + this_spot
    dirs[(0, y)] = "^"
# print(y)

for y in range(1, NUM * (maxy + 1)):
    print(get_pos_val(mapxy, 0, y, maxx+1, maxy+1), end="")
    # print("\n", y)
    
    for x in range(1, NUM * (maxx + 1)):
        # print("coord: ", (x, y), mapxy[(x, y)])
        # print(f"options: ({x}, {y - 1}) = {score_to_pos[(x, y - 1)]} | ({x - 1}, {y}) = {score_to_pos[(x - 1, y)]}")

        # print("####", score_to_pos[(x, y - 1)], score_to_pos[(x - 1, y)])
        minscore = min(score_to_pos[(x, y - 1)], score_to_pos[(x - 1, y)])
        # print("minscore: ", minscore)
        if minscore == score_to_pos[(x, y - 1)]:
            # print(x, y - 1, " | ", mapxy[(x, y - 1)])
            dirs[(x, y)] = "^"
        else:
            # print(x-1, y , " | ", mapxy[(x - 1, y)])
            dirs[(x, y)] = "<"
        # print((x, y), minscore, mapxy[(y, 0)])


        # this_spot = mapxy[(x, y)]
        this_spot = get_pos_val(mapxy, x, y, maxx+1, maxy+1)
        print(this_spot, end="")
        # print(this_spot, end="")
        score_to_pos[(x, y)] = minscore + this_spot
    print()


        # print("score to loc: ", score_to_pos[(x, y)])
        # print()
print(x, y)    
print(score_to_pos[(x, y)])

# for y in range( maxy + 1):
#     for x in range( maxx + 1):
#         print((score_to_pos[(x, y)]), end=" ")
#     print()

# print()
# print()


# for y in range( maxy + 1):
#     for x in range( maxx + 1):
#         print((dirs[(x, y)]), end=" ")
#     print()