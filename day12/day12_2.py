from collections import defaultdict

def main():
    map = read_file('input.txt')

    regions = get_regions(map)

    sum = 0

    for region in regions:
        p = list(region)[0]
        plant = map[p[0]][p[1]]
        area = len(region)
        len_sides = len(sides(region, map))
        price = area * len_sides
        print(f'A region of {plant} plants with price {area} * {len_sides} = {price}')
        sum += price

    answer = sum
    print(f'The answer: {answer}')


def sides(region, map):
    edge_pieces = get_edge_pieces(region, map)
    scan_lines = defaultdict(set)

    for ep in edge_pieces:
        if ep[2] in ['upper', 'lower']:
            scan_lines[ep[2] + str(ep[0])].add(ep[1])
        else:
            scan_lines[ep[2] + str(ep[1])].add(ep[0])

    sides = []
    for sl in scan_lines.values():
        side = []
        for i in sorted(sl):
            if len(side) == 0 or i == side[-1] + 1:
                side.append(i)
            else:
                sides.append(side)
                side = [i]
        sides.append(side)

    return sides


def get_edge_pieces(region, map):
    edge_pieces = set()

    for (y, x) in region:
        neighbours = get_neighbours(y, x, map, all=True)
        for n in neighbours:
            if not is_in_bounds(n[0], n[1], map) or map[y][x] != map[n[0]][n[1]]:
                orientation = get_orientation((y, x), n)
                edge_pieces.add((y, x, orientation))

    return edge_pieces


def get_orientation(inside, outside):
    dy = inside[0] - outside[0]
    dx = inside[1] - outside[1]

    if dy > 0:
        return 'upper'
    elif dy < 0:
        return 'lower'
    elif dx > 0:
        return 'left'
    else:
        assert dx < 0
        return 'right'


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


def get_neighbours(y, x, map, all=False):
    neighbours = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if abs(dy) + abs(dx) == 1:
                neighbour = (y + dy, x + dx)
                if all or is_in_bounds(neighbour[0], neighbour[1], map):
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
