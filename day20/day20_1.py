from collections import defaultdict


def main():
    map, start, end = read_file('input.txt')

    route = get_route(map, start, end)
    cheats = get_cheats(route, map)

    print_cheats(cheats)

    answer = at_least_100(cheats)
    print(f'The answer: {answer}')


def print_cheats(cheats):
    for saving_time in sorted(cheats.keys()):
        print(f'There are {len(cheats[saving_time])} cheats that save {saving_time} picoseconds.')


def at_least_100(cheats):
    count = 0
    for saving_time, cs in cheats.items():
        if saving_time >= 100:
            count += len(cs)
    return count


def get_cheats(route, map):
    cheats = defaultdict(list)
    for i in range(len(route) - 1):
        for neighbour, saving_time in get_cheat_neighbours(i, route, map):
            cheats[saving_time].append((route[i], neighbour))
    return cheats


def get_cheat_neighbours(i, route, map):
    neighbours = []

    pos = route[i]
    y, x = pos
    for dy in [-2, 0, 2]:
        for dx in [-2, 0, 2]:
            if abs(dy) + abs(dx) == 2 and (dy == 0 or dx == 0):
                if 0 < y + dy < len(map) and 0 < x + dx < len(map[0]):
                    if map[y + dy][x + dx] in ['.', 'E']:
                        if map[y + dy // 2][x + dx // 2] == '#':
                            neighbour = (y + dy, x + dx)
                            j = route.index(neighbour)
                            if j > i:
                                neighbours.append((neighbour, j - i - 2))

    return neighbours


def get_route(map, start, end):
    route = [start]

    while route[-1] != end:
        for neighbour in get_neighbours(route[-1], map):
            if len(route) == 1 or neighbour != route[-2]:
                route.append(neighbour)
                break

    return route


def get_neighbours(pos, map):
    neighbours = []

    y, x = pos
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if abs(dy) + abs(dx) == 1:
                if map[y + dy][x + dx] in ['.', 'E']:
                    neighbours.append((y + dy, x + dx))

    return neighbours


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    start = end = None
    map = []
    for y, line in enumerate(lines):
        map.append(line.strip())
        if 'S' in line:
            start = (y, line.index('S'))
        elif 'E' in line:
            end = (y, line.index('E'))

    return map, start, end


if __name__ == "__main__":
    main()
