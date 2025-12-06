from functools import reduce

raw_data = open("input.txt").read().splitlines()

data_p1 = [elem for elem in ' '.join(raw_data).split()]
raw_numbers_p1 = [elem for elem in data_p1 if elem.isdigit()]
nb_operations = len(data_p1) - len(raw_numbers_p1)
operations_p1 = data_p1[-nb_operations:]
rows_p1 = [raw_numbers_p1[i:i+nb_operations] for i in range(0, len(raw_numbers_p1), nb_operations)]
numbers_p1 = list(zip(*rows_p1))

part1 = sum(
    reduce(lambda a, b: eval(f"{int(a)}{operations_p1[i]}{int(b)}"), numbers_p1[i])
    for i in range(len(numbers_p1))
)

max_width = max(map(len, raw_data))
padded_lines = [line.ljust(max_width) for line in raw_data]

get_column = lambda idx: [padded_lines[row][idx] for row in range(len(padded_lines))]
is_separator = lambda col: all(c == ' ' for c in col)
extract_number = lambda col: ''.join(c for c in col[:-1] if c.isdigit())
get_operator = lambda col: col[-1] if col[-1] in ['+', '*'] else None

fold_columns = lambda acc, col_idx: (
    (acc[0] + [acc[1][::-1]], []) if is_separator(col := get_column(col_idx)) and acc[1]
    else (acc[0], acc[1] + [(extract_number(col), get_operator(col))]) if extract_number(col)
    else acc
)

problems_reversed, last_group = reduce(fold_columns, range(max_width - 1, -1, -1), ([], []))
problems = problems_reversed + ([last_group[::-1]] if last_group else [])

part2 = sum(
    reduce(lambda a, b: eval(f"{a}{next(o for _, o in prob if o)}{b}"), [int(n) for n, _ in prob])
    for prob in problems
)

print(f"part1: {part1}")
print(f"part2: {part2}")