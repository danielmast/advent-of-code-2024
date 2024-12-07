def main():
    start_y, start_x, original_map = read_file('input.txt')

    options_count = 0

    visited = get_visited(original_map, start_y, start_x)

    for r, c in visited:
        print('options_count =', options_count)
        map = create_map_with_obstacle(original_map, r, c)

        y = start_y
        x = start_x
        direction = 'up'

        crumbs = [(y, x, direction)]

        while True:
            next_y, next_x = next_location(y, x, direction)
            if (next_y < 0 or next_y >= len(map) or
                    next_x < 0 or next_x >= len(map[0])):
                break
            elif map[next_y][next_x] in ['#', 'O']:
                direction = turn_right(direction)
            else:
                y = next_y
                x = next_x
                if (y, x, direction) in crumbs:
                    options_count += 1
                    break
                else:
                    crumbs.append((y, x, direction))

    answer = options_count
    print(f'The answer: {answer}')


def get_visited(map, y, x):
    visited = set()

    direction = 'up'

    while True:
        next_y, next_x = next_location(y, x, direction)
        if (next_y < 0 or next_y >= len(map) or
                next_x < 0 or next_x >= len(map[0])):
            break
        elif map[next_y][next_x] == '#':
            direction = turn_right(direction)
        else:
            y = next_y
            x = next_x
            visited.add((y, x))

    return visited


def create_map_with_obstacle(map, y, x):
    map_with_obstacle = map.copy()
    row = map[y]
    map_with_obstacle[y] = row[:x] + 'O' + row[x + 1:]
    return map_with_obstacle


def next_location(y, x, direction):
    if direction == 'up':
        return y - 1, x
    elif direction == 'right':
        return y, x + 1
    elif direction == 'down':
        return y + 1, x
    else:
        return y, x - 1


def turn_right(direction):
    if direction == 'up':
        return 'right'
    elif direction == 'right':
        return 'down'
    elif direction == 'down':
        return 'left'
    else:
        return 'up'


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()
    lines = [line.strip() for line in lines]

    for l, line in enumerate(lines):
        if '^' in line:
            return l, line.index('^'), lines


if __name__ == "__main__":
    main()
