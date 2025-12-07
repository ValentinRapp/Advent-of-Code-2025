# part 2 copied from https://github.com/fuglede/adventofcode/blob/master/2025/day07/solutions2.py
# I didn't have time

data = [list(row) for row in open("input.txt").read().split()]

def nb_splits(data: list[list[str]]):
    splits = 0
    for i in range(len(data) - 1):
        if 'S' in data[i]:
            data[i][data[i].index('S')] = '|'
        for j in range(len(data[i])):
            if data[i][j] == '|' and data[i+1][j] == '^':
                data[i+1][j+1] = '|'
                data[i+1][j-1] = '|'
                splits += 1
            elif data[i][j] == '|' and data[i+1][j] == '.':
                data[i+1][j] = '|'
    return splits

def nb_timelines(grid: list[list[str]]):
    splitters = [col for row in grid for col, x in enumerate(row) if x == '^']
    entering = [1] + [0] * (len(splitters) - 1)
    for i, si in enumerate(splitters):
        for j, sj in enumerate(splitters[:i][::-1]):
            if si == sj:
                break
            if abs(si - sj) == 1:
                entering[i] += entering[i - j - 1]
    return sum(entering) + 1

part1 = nb_splits([row[:] for row in data])
part2 = nb_timelines(data)

print(f"part1: {part1}")
print(f"part2: {part2}")