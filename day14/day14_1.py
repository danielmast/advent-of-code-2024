import re
from math import prod


def main():
    robots = read_file('input.txt')

    width = 101
    height = 103
    seconds = 100

    for robot in robots:
        robot.move(width, height, seconds)

    answer = safety_factor(robots, width, height)
    print(f'The answer: {answer}')


def safety_factor(robots, width, height):
    middle_x = width // 2
    middle_y = height // 2

    quadrants = [[],[],[],[]]

    for robot in robots:
        if robot.p.x < middle_x and robot.p.y < middle_y:
            quadrants[0].append(robot)
        elif robot.p.x < middle_x and robot.p.y > middle_y:
            quadrants[1].append(robot)
        elif robot.p.x > middle_x and robot.p.y < middle_y:
            quadrants[2].append(robot)
        elif robot.p.x > middle_x and robot.p.y > middle_y:
            quadrants[3].append(robot)

    return prod([len(quadrant) for quadrant in quadrants])


class Robot:
    def __init__(self, p, v):
        self.p = p
        self.v = v

    def move(self, width, height, seconds):
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
