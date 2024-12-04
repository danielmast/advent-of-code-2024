

def main():
    input = read_file('input.txt')
    print(f'The answer: {solve(input)}')


def is_xmas(y, x, input):
    if y == 0 or y == len(input) - 1:
        return False

    if x == 0 or x == len(input) - 1:
        return False

    if input[y][x] != 'A':
        return False

    top_left = input[y-1][x-1]
    top_right = input[y-1][x+1]
    bottom_left = input[y+1][x-1]
    bottom_right = input[y+1][x+1]

    ms = ['M', 'S']

    if top_left not in ms or top_right not in ms or bottom_left not in ms or bottom_right not in ms:
        return False

    if top_left == bottom_right:
        return False

    if top_right == bottom_left:
        return False

    return True


def solve(input):
    n = len(input)
    sum = 0

    for y in range(0, n):
        for x in range(0, n):
            if is_xmas(y, x, input):
                sum += 1

    return sum


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    result = []

    for line in lines:
        result.append(line.strip())

    return result


if __name__ == "__main__":
    main()
