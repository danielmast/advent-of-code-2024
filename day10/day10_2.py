def main():
    map = read_file('input.txt')

    trailheads = get_trailheads(map)
    sum = 0

    for t in trailheads:
        score = paths_to_top(t[0], t[1], map)
        sum += score

    answer = sum
    print(f'The answer: {answer}')


def get_trailheads(map):
    trailheads = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 0:
                trailheads.append((y, x))
    return trailheads


def paths_to_top(y, x, map):
    if map[y][x] == 9:
        return 1

    paths = 0

    for neighbour in get_neighbours(y, x, map):
        if map[neighbour[0]][neighbour[1]] == map[y][x] + 1:
            paths += paths_to_top(neighbour[0], neighbour[1], map)

    return paths


def get_neighbours(y, x, map):
    neighbours = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if abs(dy) + abs(dx) == 1:
                neighbour = (y + dy, x + dx)
                if is_in_bounds(neighbour[0], neighbour[1], map):
                    neighbours.append(neighbour)

    return neighbours


def is_in_bounds(y, x, map):
    return 0 <= y < len(map) and 0 <= x < len(map[0])


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    map = [[int(i) for i in line.strip()] for line in lines]

    return map


if __name__ == "__main__":
    main()
