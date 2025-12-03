from functools import reduce

data = [elem for elem in open("input.txt").read().split()]

def find_max_joltage(b: str, n: int) -> int:
    pick = lambda acc, _ :\
        (acc[0] + b[(idx := max(range(acc[1], len(b) - acc[2] + 1), key=lambda i : b[i]))], idx + 1, acc[2] - 1)
    return int(reduce(pick, range(n), ('', 0, n))[0])

print(f"part1: {sum(map(lambda b: find_max_joltage(b, 2), data))}")
print(f"part2: {sum(map(lambda b: find_max_joltage(b, 12), data))}")
