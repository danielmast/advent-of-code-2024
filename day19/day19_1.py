def main():
    patterns, designs = read_file('input.txt')

    possible_count = sum([int(is_possible(design, patterns)) for design in designs])

    answer = possible_count
    print(f'The answer: {answer}')


def is_possible(design, patterns):
    wips = {''}

    while design not in wips:
        new_wips = set()
        for wip in wips:
            for pattern in patterns:
                if design.startswith(wip + pattern):
                    new_wips.add(wip + pattern)

        if wips == new_wips:
            return False

        wips = new_wips

    return True


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    patterns = lines[0].replace(' ', '').strip().split(',')
    designs = []

    for line in lines[2:]:
        designs.append(line.strip())

    return patterns, designs


if __name__ == "__main__":
    main()
