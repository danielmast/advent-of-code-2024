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
    next = get_next(robot, move)

    if map[next[0]][next[1]] == '#':
        return

    if map[next[0]][next[1]] == '.':
        map[next[0]][next[1]] = '@'
        map[robot[0]][robot[1]] = '.'
        return

    if map[next[0]][next[1]] == 'O':
        do_move_boxes(robot, move, map, next)


def do_move_boxes(robot, move, map, next):
    next_box = next
    boxes = [next_box]
    next_box = get_next(next_box, move)
    while map[next_box[0]][next_box[1]] == 'O':
        boxes.append(next_box)
        next_box = get_next(next_box, move)

    if map[next_box[0]][next_box[1]] != '.':
        return

    boxes.reverse()
    for box in boxes:
        next = get_next(box, move)
        map[next[0]][next[1]] = 'O'
        map[box[0]][box[1]] = '.'

    next = get_next(robot, move)
    map[next[0]][next[1]] = '@'
    map[robot[0]][robot[1]] = '.'


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
            if column == 'O':
                sum += 100 * r + c
    return sum


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    map = []
    moves = []

    is_reading_map = True

    for line in [line.strip() for line in lines]:
        if not line:
            is_reading_map = False
        elif is_reading_map:
            row = list(line)
            map.append(row)
        else:
            moves += list(line)

    return map, moves


if __name__ == "__main__":
    main()
