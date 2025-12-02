data = [
    num 
        for elem in open("input.txt").read().split(',')
        for num in range(int(elem.split('-')[0]), int(elem.split('-')[1]) + 1)
]

def is_invalid_ID_part1(ID: str) -> bool:
    s = str(int(ID))
    n = len(s)
    return n > 0 and n % 2 == 0 and s[: n // 2] == s[n // 2 :]

def is_invalid_ID_part2(ID: str) -> bool:
    s = str(int(ID))
    n = len(s)
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            pattern = s[:length]
            if pattern * (n // length) == s:
                return True
    return False

part1 = sum(filter(lambda elem : is_invalid_ID_part1(str(elem)), data))
part2 = sum(filter(lambda elem : is_invalid_ID_part2(str(elem)), data))

print(f"part1: {part1}\npart2: {part2}")
