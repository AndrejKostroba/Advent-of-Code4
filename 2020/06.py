from string import ascii_lowercase as letters

with open('06.txt', 'r') as file:
    data = file.read().split('\n\n')


def part_one(data):
    res = 0
    for line in data:
        cur = set()
        for s in line.split():
            cur |= set(s)
        res += len(cur)
    return res


def part_two(data):
    res = 0
    for line in data:
        cur = set(letters)
        for s in line.split():
            cur &= set(s)
        res += len(cur)
    return res


if __name__ == '__main__':
    print(f'Part 1: {part_one(data)}')  # 6775
    print(f'Part 2: {part_two(data)}')  # 3356
