def main():
    y, x, map = read_file('input.txt')

    visited = map.copy()
    visited[y] = visited[y][:x] + 'X' + visited[y][x + 1:]

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
            visited[y] = visited[y][:x] + 'X' + visited[y][x + 1:]

    visited_count = 0
    for line in visited:
        for c in line:
            if c == 'X':
                visited_count += 1

    answer = visited_count
    print(f'The answer: {answer}')


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
