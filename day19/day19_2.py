def main():
    patterns, designs = read_file('input.txt')

    possible_count = 0
    for design in designs:
        possible_count += num_options(design, patterns)

    answer = possible_count
    print(f'The answer: {answer}')


memo = {
    '': 1
}


def num_options(design, patterns):
    global memo

    if design in memo.keys():
        return memo[design]

    count = 0

    for pattern in patterns:
        if design.startswith(pattern):
            count += num_options(design[len(pattern):], patterns)

    memo[design] = count
    return count


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
