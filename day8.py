def get_data(filename):
    data = []
    line_tups = []
    with open(filename, 'r') as f:
        for line in f:
            print(line)
            egs, values = line.split(" | ")
            egs = egs.split()
            values = values.split()
            line_tups.append((egs, values))
    return line_tups

data = get_data("day8.txt")

"""
0:6
1:2
2:5
3:5
4:4
5:5
6:6
7:3
8:7
9:6
"""

# count = 0
# for egs, values in line_tups: 
#     for v in values:
#         print(v)
#         if len(v) in [2,3,4,7]:
#             count += 1
# print(count)

def sort_str(string):
    sort_letters = "".join(sorted(list(string)))
    return sort_letters

def get_dif_seg(num_map, superseg, subseg):
    set_super = list(num_map[superseg])
    set_sub = num_map[subseg]
    for letter in set_sub:
        set_super.remove(letter)
    return set_super[0]

def remove_seg(set_num, seg_list, wire_map, num_map):
        remaining_segs = list(num_map[set_num])
        for letter in seg_list:
            remaining_segs.remove(wire_map[letter])
        return remaining_segs

from collections import defaultdict


def get_num_output(egs, values):

    num_map = {}
    wire_map = {}
    len_maps = defaultdict(list)

    for eg in egs:
        if len(eg) == 2:
            num_map[1] = eg
        elif len(eg) == 3:
            num_map[7] = eg
        elif len(eg) == 4:
            num_map[4] = eg
        elif len(eg) == 7:
            num_map[8] = eg 
        else:
            len_maps[len(eg)].append(eg)

    #find seg a (7 without 1)
    dif_7_1 = get_dif_seg(num_map, superseg=7, subseg=1)
    wire_map["a"] = dif_7_1


    #find num 6 (len 6 without both of a and c)
    for op in len_maps[6]:
        set_1 = num_map[1]
        print(op)
        if not set_1[0] in op or not set_1[1] in op:
            num_map[6] = op
            len_maps[6].remove(op)
            break
    else:
        raise Exception("6 not found")

    # get seg c (8 without 6)
    dif_8_6 = get_dif_seg(num_map, superseg=8, subseg=6)
    wire_map["c"] = dif_8_6

    # get seg f (7 without a and c)
    remaining_segs = remove_seg(set_num=7, seg_list=["a", "c"], wire_map=wire_map, num_map=num_map)
    wire_map["f"] = remaining_segs[0]

    # Find 9 (len 6, contains all of set 4)
    for op in len_maps[6]:
        set_4 = num_map[4]
        if all([letter in op for letter in set_4]):
            num_map[9] = op
            len_maps[6].remove(op)
            break
    else:
        raise Exception("9 not found") 

    # Find 0 (only len 6 remaining)
    num_map[0] = len_maps[6][0]

    # get seg d (set 8 without set 0)
    dif_8_0 = get_dif_seg(num_map, superseg=8, subseg=0)
    wire_map["d"] = dif_8_0

    # get seg b (set 4 without d, c, f)
    remaining_segs = remove_seg(set_num=4, seg_list=["d", "c", "f"], wire_map=wire_map,  num_map=num_map)
    wire_map["b"] = remaining_segs[0]

    # get seg g (set 9 without abcdf)
    remaining_segs = remove_seg(set_num=9, seg_list=["a", "b", "c", "d", "f"], wire_map=wire_map,  num_map=num_map)
    wire_map["g"] = remaining_segs[0]

    # get seg e (set 8 without set 9)
    remaining_segs = get_dif_seg(num_map, superseg=8, subseg=9)
    wire_map["e"] = remaining_segs[0]




    map_num_to_norm_letter = {
    0: "abcefg",
    1:"cf",
    2:"acdeg",
    3:"acdfg",
    4:"bcdf",
    5:"abdfg",
    6:"abdefg",
    7:"acf",
    8:"abcdefg",
    9:"abcdfg"}

    map_norm_letter_to_num = {let: num for num, let in map_num_to_norm_letter.items()}

    print(num_map)
    map_bad_let_to_num = {}
    for letters, num in map_norm_letter_to_num.items():
        bad_letters = ""
        for letter in letters:
            bad_letter = wire_map[letter]
            bad_letters = bad_letters + bad_letter
        map_bad_let_to_num["".join(sorted(list(bad_letters)))] = num
    map_num_to_bad_let = {v: k for k,v in map_bad_let_to_num.items()}

    print()
    for i in range(10):
        print(i, sort_str(num_map.get(i, "---")), sort_str(map_num_to_bad_let[i]), sort_str(num_map.get(i, "---")) == sort_str(map_num_to_bad_let[i]))
    print()    
    print("#", num_map)
    print("$", map_bad_let_to_num)

    print(wire_map)


    test_dict = {"acedgfb": 8,
    "cdfbe": 5,
    "gcdfa": 2,
    "fbcad": 3,
    "dab": 7,
    "cefabd": 9,
    "cdfgeb": 6,
    "eafb": 4,
    "cagedb": 0,
    "ab": 1}

    test_dict = {sort_str(k): v for k,v in test_dict.items()}
    print(test_dict)
    for bl, bn in map_bad_let_to_num.items():
        if bl not in test_dict:
            print("Error", bl, bn)


    num = ""
    for v in values:
        v_sort = "".join(sorted(list(v)))
        num += str(map_bad_let_to_num[v_sort])
    num = int(num)
        
    return num 

nums = []
for egs, values in data: 
    num = get_num_output(egs, values)
    nums.append(num)
print(sum(nums))


# print(num_map)


# def letters_to_num(letters):
    


