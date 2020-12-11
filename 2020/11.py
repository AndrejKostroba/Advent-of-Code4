with open('11.txt', 'r') as file:
    data = file.read()

def parse_input(data):
    return [list(line) for line in data.split('\n')]

data = parse_input(data)
N, M = len(data), len(data[0])

from tools import timer


def get_state(data):
    occupied, empty = set(), set()
    for i in range(N):
        for j in range(M):
            if data[i][j] == '#':
                occupied.add((i, j))
            if data[i][j] == 'L':
                empty.add((i, j))
    return occupied, empty


def check_seat_one(seat_pos, occupied):
    x, y = seat_pos
    count = 0
    for dx, dy in [(1,0), (1,1), (0,1), (-1,0), (-1,1), (0,-1), (-1,-1), (1,-1)]:
        if (x+dx, y+dy) in occupied:
            count += 1
    return count

@timer
def part_one(data):
    occupied, empty = get_state(data)
    while True:
        occupy = set()
        deoccupy = set()
        for seat in empty:
            if check_seat_one(seat, occupied) == 0:
                occupy.add(seat)
        for seat in occupied:
            if check_seat_one(seat, occupied) >= 4:
                deoccupy.add(seat)
        if not occupy and not deoccupy:
            break
        occupied -= deoccupy
        occupied |= occupy
        empty -= occupy
        empty |= deoccupy
    return len(occupied)


def check_seat_two(seat_pos, occupied, data):
    x, y = seat_pos
    count = 0
    for dx, dy in [(1,0), (1,1), (0,1), (-1,0), (-1,1), (0,-1), (-1,-1), (1,-1)]:
        cur_x, cur_y = x+dx, y+dy
        while 0 <= cur_x < N and 0 <= cur_y < M and data[cur_x][cur_y] == '.':
            cur_x += dx
            cur_y += dy
        if (cur_x, cur_y) in occupied:
            count += 1
    return count


@timer
def part_two(data):
    occupied, empty = get_state(data)
    while True:
        occupy = set()
        deoccupy = set()
        for seat in empty:
            if check_seat_two(seat, occupied, data) == 0:
                occupy.add(seat)
        for seat in occupied:
            if check_seat_two(seat, occupied, data) >= 5:
                deoccupy.add(seat)
        if not occupy and not deoccupy:
            break
        occupied -= deoccupy
        occupied |= occupy
        empty -= occupy
        empty |= deoccupy
    return len(occupied)


print(f'Part 1: {part_one(data)}')  # 2472
print(f'Part 2: {part_two(data)}')  # 2197
