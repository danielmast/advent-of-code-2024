import re

def main():
    lines = read_file('input.txt')
    input = ''.join(lines)

    mul_matches = re.finditer(r"mul\(([0-9]+),([0-9]+)\)", input)
    do_matches = re.finditer(r"(do\(\))", input)
    dont_matches = re.finditer(r"(don't\(\))", input)

    actions = [None] * len(input)

    for match in do_matches:
        actions[match.start()] = 'do'

    for match in dont_matches:
        actions[match.start()] = 'dont'

    for match in mul_matches:
        product = int(match.groups()[0]) * int(match.groups()[1])
        actions[match.start()] = product

    sum = 0

    enabled = True
    for action in actions:
        if isinstance(action, int) and enabled:
            sum += int(action)
        elif action == 'do':
            enabled = True
        elif action == 'dont':
            enabled = False

    answer = sum
    print(f'The answer: {answer}')


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines


if __name__ == "__main__":
    main()
