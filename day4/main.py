# I know this is pretty nasty and verbose

class Grid:
    data: list[list[str]]
    forklifts: list[tuple[int, int]]

    def __init__(self, data: str) -> None:
        self.data = [list(row) for row in data.split()]
        self.update_forklifts()

    def update_forklifts(self) -> None:
        self.forklifts = [(x, y) for y, row in enumerate(self.data) for x, char in enumerate(row) if char == '@']

    def erase_forklift(self, coord: tuple[int, int]) -> None:
        self.data[coord[1]][coord[0]] = '.'

def count_neighbours(data: list[list[str]], coord: tuple[int, int]) -> int:
    s = 0
    dy = [-1, -1, -1,  0,  0,  1,  1,  1]
    dx = [-1,  0,  1, -1,  1, -1,  0,  1]

    for i in range(8):
        ny = coord[1] + dy[i]
        nx = coord[0] + dx[i]
        if (ny >= 0 and ny < len(data) and nx >= 0 and nx < len(data[0])):
            s += 1 if data[ny][nx] == '@' else 0

    return s

grid = Grid(open("input.txt").read())

part1 = sum([count_neighbours(grid.data, elem) < 4 for elem in grid.forklifts])

part2 = 0

while (forklifts := [f for f in grid.forklifts if count_neighbours(grid.data, f) < 4]):
    part2 += len(forklifts)
    for forklift in forklifts: grid.erase_forklift(forklift)
    grid.update_forklifts()

print(f"part1: {part1}")
print(f"part2: {part2}")
