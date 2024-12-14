import re
from collections import defaultdict


def main():
    robots = read_file('input.txt')

    width = 101
    height = 103

    s = 1
    while True:
        print(f'Seconds: {s}')

        for robot in robots:
            robot.move(width, height)

        map = get_map(robots)

        if is_christmas_tree(map):
            print_map(map, width, height)
            answer = s
            print(f'The answer: {answer}')
            break

        s += 1


def is_christmas_tree(map):
    return has_no_collisions(map)


def has_no_collisions(map):
    for y in map.keys():
        for v in map[y].values():
            if v > 1:
                return False
    return True


def get_map(robots):
    map = defaultdict(lambda: defaultdict(int))

    for robot in robots:
        map[robot.p.y][robot.p.x] += 1

    return map


def print_map(map, width, height):
    for y in range(height):
        line = ''
        for x in range(width):
            if map[y][x] > 9:
                line += '+'
            elif map[y][x] > 0:
                line += str(map[y][x])
            else:
                line += '_'
        print(line)
    print()
    print()


class Robot:
    def __init__(self, p, v):
        self.p = p
        self.v = v

    def move(self, width, height, seconds=1):
        self.p.x = (self.p.x + seconds * self.v.x) % width
        self.p.y = (self.p.y + seconds * self.v.y) % height

    def __str__(self):
        return f'p={self.p} v={self.v}'


class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    robots = []

    for line in lines:
        matches = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line.strip()).groups()
        robot = Robot(
            p=XY(x=int(matches[0]), y=int(matches[1])),
            v=XY(x=int(matches[2]), y=int(matches[3]))
        )
        robots.append(robot)

    return robots


if __name__ == "__main__":
    main()
