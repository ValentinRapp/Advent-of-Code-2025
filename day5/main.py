from bisect import bisect_right
from functools import reduce

raw_data = open("input.txt").read().rstrip()
block1, block2 = raw_data.split("\n\n", 1)

parse_interval = lambda line: tuple(int(elem) for elem in line.split("-"))
intervals = sorted(map(parse_interval, block1.splitlines()))

merge = lambda acc, ab: (
    acc[:-1] + [(acc[-1][0], max(acc[-1][1], ab[1]))]
    if acc and ab[0] <= acc[-1][1] + 1
    else acc + [ab]
)
valid_IDs_ranges = reduce(merge, intervals, [])

starts = [s for s, _ in valid_IDs_ranges]
is_valid = lambda x:\
    (i := bisect_right(starts, x) - 1) >= 0 and valid_IDs_ranges[i][0] <= x <= valid_IDs_ranges[i][1]

IDs_to_check = [int(ID) for ID in block2.splitlines()]

nb_valid_IDs = sum(map(is_valid, IDs_to_check))
nb_fresh = sum(b - a + 1 for a, b in valid_IDs_ranges)

print(f"part1: {nb_valid_IDs}")
print(f"part2: {nb_fresh}")
