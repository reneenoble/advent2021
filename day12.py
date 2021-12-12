class Cave():
    def __init__(self, name):
        self.name = name
        if name.islower():
            self.small = True
        else:
            self.small = False
        self.neighs = set()
    
    def add_neighbour(self, neigh):
        self.neighs.add(neigh)

    def router(self, visited_nodes=[], small_visited=False):
        count = 0
        if self.name == "end":
            return 1
        else:
            paths = 0
            visited_nodes.append(self)
            
            eligible_neighs = [n for n in self.neighs if not (n.small and n in visited_nodes and small_visited) and not n.name == "start"]          
            for neigh in eligible_neighs:
                next_small_visited = small_visited or (neigh.small and neigh in visited_nodes)
                ended = neigh.router(visited_nodes[:], next_small_visited)
                count += ended
            return count


def get_data(filename):
    edges = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split("-")
            edges.append(tuple(line))
    return edges


edges = get_data("day12.txt")
cave_names = set()
for a, b in edges:
    cave_names.add(a)
    cave_names.add(b)

# Build nodes
cave_dict = {}
for cave_name in cave_names:
    cave_dict[cave_name] = Cave(cave_name)

# Add edges
for a, b in edges:
    cave_a = cave_dict[a]
    cave_b = cave_dict[b]
    cave_a.add_neighbour(cave_b)
    cave_b.add_neighbour(cave_a)


# routes = []
start = cave_dict["start"]
num = start.router()
print(num)
