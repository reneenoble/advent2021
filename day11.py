SIZE = 10

class Octo():
    def __init__(self, x, y, num):
        self.num = int(num)
        self.x = x
        self.y = y
        self.neighs = None
        self.flashed = False

    def start_stage(self):
        self.flashed = False
        if self.num > 9:
            self.num = 0

    def increment(self):
        if not self.flashed:
            self.num += 1
            if self.num > 9:
                self.flashed = True
                for neigh in self.neighs:
                    if not neigh.flashed:
                        neigh.increment()

    def set_neighs(self, mapxy, maxx=0, maxy=9):
        neigh_nodes = []
        if self.x - 1 >= 0:
            neigh_nodes.append(mapxy[(self.x - 1, self.y)])
        if self.x + 1 <= maxx:
            neigh_nodes.append(mapxy[(self.x + 1, self.y)])
        if self.y - 1 >= 0:
            neigh_nodes.append(mapxy[(self.x, self.y - 1)])
        if self.y + 1 <= maxy:
            neigh_nodes.append(mapxy[(self.x, self.y + 1)])
        if self.x - 1 >= 0 and self.y - 1 >= 0:
            neigh_nodes.append(mapxy[(self.x - 1, self.y - 1)])
        if self.x - 1 >= 0 and self.y + 1 <= maxx:
            neigh_nodes.append(mapxy[(self.x - 1, self.y + 1)])
        if self.x + 1 <= maxx and self.y - 1 >= 0:
            neigh_nodes.append(mapxy[(self.x + 1, self.y - 1)])
        if self.x + 1 <= maxx and self.y + 1 <= maxy:
            neigh_nodes.append(mapxy[(self.x + 1, self.y + 1)])
        
        self.neighs = neigh_nodes

def get_data(filename):
    mapxy = {}
    with open(filename, 'r') as f:
        for y, line in enumerate(f):
            line = list(line.strip())
            for x, num in enumerate(line):
                mapxy[(x, y)] = Octo(x, y, num)

    for oct in mapxy.values():
        oct.set_neighs(mapxy, x, y)
    return mapxy


mapxy = get_data("day11.txt")


flashes = 0
count = 1
while True:

    for octo in mapxy.values():
        octo.increment()

    total = sum([1 for octo in mapxy.values() if octo.flashed])
    flashes += total
    if total == SIZE**2:
        break

    for octo in mapxy.values():
        octo.start_stage()
        
    count += 1

print("Flashes", flashes)
print(count)