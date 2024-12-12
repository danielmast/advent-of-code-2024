def main():
    map = read_file('input.txt')

    regions = get_regions(map)

    sum = 0
    for region in regions:
        sum += len(region) * perimeter(region, map)
    answer = sum

    print(f'The answer: {answer}')


def perimeter(region, map):
    result = 0
    for (y, x) in region:
        neighbours = get_neighbours(y, x, map)
        result += 4 - len(neighbours)  # Edge of the map
        for n in neighbours:
            if map[y][x] != map[n[0]][n[1]]:
                result += 1
    return result


def get_regions(map):
    regions = []
    explored = set()

    for y in range(len(map)):
        for x in range(len(map[0])):
            p = (y, x)
            if p in explored:
                continue

            region = expand_region({p}, map)
            regions.append(region)
            explored = explored.union(region)

    return regions


def expand_region(region, map):
    expanded = region.copy()
    for p in region:
        for n in get_neighbours(p[0], p[1], map):
            if map[p[0]][p[1]] == map[n[0]][n[1]] and n not in expanded:
                expanded.add(n)

    if len(region) == len(expanded):
        return expanded
    else:
        return expand_region(expanded, map)


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

    map = [line.strip() for line in lines]

    return map


if __name__ == "__main__":
    main()
