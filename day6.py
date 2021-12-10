def get_data(filename):
    data = []
    with open(filename, 'r') as f:
        data = [int(i) for i in f.read().strip().split(",")]
    return data


fishes = get_data("day6demo.txt")

# class Fish():
#     def __init__(self, num=8):
#         self.counter = num
    
#     def new_day(self):
#         if self.counter == 0:
#             self.counter = 6
#         else: 
#             self.counter -= 1
        

    
# for i in range(80):
#     new_fishes = []
#     babies = []
#     for fish in fishes:
#         if fish == 0:
#             new_fishes.append(6)
#             babies.append(8)
#         else: 
#             new_fishes.append(fish - 1)
#     fishes = new_fishes + babies


from collections import defaultdict

groups = defaultdict(int)
for fish in fishes:
    groups[fish] += 1

for day in range(256):
    new_groups = {fish - 1: count for fish, count in groups.items() if fish != 0}
    new_groups[8] = groups.get(0, 0)
    new_groups[6] = new_groups.get(6, 0) + groups.get(0, 0)
    groups = new_groups
print(sum(groups.values()))