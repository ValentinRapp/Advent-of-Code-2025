from math import sqrt

data: list[tuple[int, int, int]] = [
    tuple(map(lambda x : int(x), row.split(',')))  # type: ignore
    for row in open("input.txt").read().split()
]

def length(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return sqrt(sum((a[i] - b[i]) ** 2 for i in range(3)))

distances = [(length(a, b), i, j) for i, a in enumerate(data) for j, b in enumerate(data) if i < j]
distances.sort()

parent = {i: i for i in range(len(data))}
size = {i: 1 for i in range(len(data))}

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x == root_y:
        return False
    if size[root_x] < size[root_y]:
        root_x, root_y = root_y, root_x
    parent[root_y] = root_x
    size[root_x] += size[root_y]
    return True

parent_p1 = {i: i for i in range(len(data))}
size_p1 = {i: 1 for i in range(len(data))}

def find_p1(x):
    if parent_p1[x] != x:
        parent_p1[x] = find_p1(parent_p1[x])
    return parent_p1[x]

def union_p1(x, y):
    root_x, root_y = find_p1(x), find_p1(y)
    if root_x == root_y:
        return False
    if size_p1[root_x] < size_p1[root_y]:
        root_x, root_y = root_y, root_x
    parent_p1[root_y] = root_x
    size_p1[root_x] += size_p1[root_y]
    return True

connections = 0
for dist, i, j in distances:
    if connections >= 1000:
        break
    connections += 1
    union_p1(i, j)

circuit_sizes_p1 = {}
for i in range(len(data)):
    root = find_p1(i)
    circuit_sizes_p1[root] = size_p1[root]

top3 = sorted(circuit_sizes_p1.values(), reverse=True)[:3]
while len(top3) < 3:
    top3.append(1)

part1 = top3[0] * top3[1] * top3[2]

parent_p2 = {i: i for i in range(len(data))}
size_p2 = {i: 1 for i in range(len(data))}
num_circuits = len(data)

def find_p2(x):
    if parent_p2[x] != x:
        parent_p2[x] = find_p2(parent_p2[x])
    return parent_p2[x]

def union_p2(x, y):
    global num_circuits
    root_x, root_y = find_p2(x), find_p2(y)
    if root_x == root_y:
        return False
    if size_p2[root_x] < size_p2[root_y]:
        root_x, root_y = root_y, root_x
    parent_p2[root_y] = root_x
    size_p2[root_x] += size_p2[root_y]
    num_circuits -= 1
    return True

last_i, last_j = 0, 0
for dist, i, j in distances:
    if union_p2(i, j):
        last_i, last_j = i, j
        if num_circuits == 1:
            break

part2 = data[last_i][0] * data[last_j][0]

print(f"part1: {part1}")
print(f"part2: {part2}")