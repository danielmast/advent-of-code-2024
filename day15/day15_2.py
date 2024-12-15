def main():
    map, moves = read_file('input.txt')

    print('Initial state:')
    print_map(map)

    for move in moves:
        do_move(move, map)

    print('Final state:')
    print_map(map)

    answer = gps_sum(map)
    print(f'The answer: {answer}')


def print_map(map):
    for row in map:
        print(''.join(row))
    print()


def do_move(move, map):
    robot = get_robot(map)

    if can_push(robot, move, map):
        push(robot, move, map)


def get_counterpart(box, map):
    if get(map, box) == '[':
        return box[0], box[1] + 1

    assert map[box[0]][box[1]] == ']'

    return box[0], box[1] - 1


def get(map, position):
    return map[position[0]][position[1]]


def set(map, position, value):
    map[position[0]][position[1]] = value


def can_push(current, move, map):
    next = get_next(current, move)

    if get(map, next) == '#':
        return False

    if get(map, next) == '.':
        return True

    assert get(map, next) in ['[', ']']

    result = can_push(next, move, map)

    if move in ['v', '^']:
        next_counterpart = get_counterpart(next, map)
        result = result and can_push(next_counterpart, move, map)

    return result


def push(current, move, map):
    next = get_next(current, move)
    if get(map, next) == '.':
        set(map, next, get(map, current))
        set(map, current, '.')
    else:
        cp = None
        if move in ['v', '^']:
            cp = get_counterpart(next, map)

        push(next, move, map)
        assert get(map, next) == '.'

        if cp:
            push(cp, move, map)
            assert get(map, cp) == '.'

        set(map, next, get(map, current))
        set(map, current, '.')


def get_next(robot, move):
    if move == '<':
        return robot[0], robot[1] - 1
    elif move == '>':
        return robot[0], robot[1] + 1
    elif move == '^':
        return robot[0] - 1, robot[1]
    else:  # v
        return robot[0] + 1, robot[1]


def get_robot(map):
    for r, row in enumerate(map):
        for c, column in enumerate(row):
            if map[r][c] == '@':
                return r, c


def gps_sum(map):
    sum = 0
    for r, row in enumerate(map):
        for c, column in enumerate(row):
            if column == '[':
                sum += 100 * r + c
    return sum


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    map = []
    moves = []

    is_reading_map = True

    for r, line in enumerate([line.strip() for line in lines]):
        if not line:
            is_reading_map = False
        elif is_reading_map:
            row = []

            for c, column in enumerate(line):
                if column == '#':
                    row += ['#'] * 2
                elif column == 'O':
                    row += ['[', ']']
                elif column == '.':
                    row += ['.'] * 2
                else:
                    assert column == '@'
                    row += ['@', '.']

            map.append(row)
        else:
            moves += list(line)

    return map, moves


if __name__ == "__main__":
    main()
