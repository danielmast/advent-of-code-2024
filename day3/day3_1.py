import re

def main():
    lines = read_file('input.txt')

    sum = 0

    for line in lines:
        matches = re.findall(r"mul\(([0-9]+),([0-9]+)\)", line)

        for match in matches:
            sum += int(match[0]) * int(match[1])

    answer = sum
    print(f'The answer: {answer}')


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
