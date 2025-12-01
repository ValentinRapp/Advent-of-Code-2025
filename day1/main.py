
class Dial:
    def __init__(self, initial_value: int, dial_size: int, part1: bool) -> None:
        self.value = initial_value % dial_size
        self.dial_size = dial_size
        self.password = 0
        self.part1 = part1

    def rotate(self, instruction: str) -> None:
        d = 1 if instruction[0] == 'R' else -1
        end = self.value + int(instruction[1:]) * d
        if not self.part1:
            self.password += d * ((end - (1-d)//2) // self.dial_size - (self.value - (1-d)//2) // self.dial_size)
        else:
            self.password += end % self.dial_size == 0
        self.value = end % self.dial_size

with open("input.txt", "r") as file:
    data = file.read().splitlines()

dial1 = Dial(50, 100, True)
dial2 = Dial(50, 100, False)

list(map(lambda elem : dial1.rotate(elem), data))
list(map(lambda elem : dial2.rotate(elem), data))

print(f"part1: {dial1.password}\npart2: {dial2.password}")
