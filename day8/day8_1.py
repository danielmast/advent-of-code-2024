def main():
    antennas, dim = read_file('input.txt')

    antinodes = set()

    for i in range(len(antennas)):
        for j in range(len(antennas)):
            if i == j or antennas[i][2] != antennas[j][2]:
                continue

            diff_y = antennas[i][0] - antennas[j][0]
            diff_x = antennas[i][1] - antennas[j][1]

            antinode1 = (antennas[i][0] + diff_y, antennas[i][1] + diff_x)
            antinode2 = (antennas[j][0] - diff_y, antennas[j][1] - diff_x)

            if is_on_map(antinode1, dim):
                antinodes.add(antinode1)
            if is_on_map(antinode2, dim):
                antinodes.add(antinode2)

    answer = len(antinodes)
    print(f'The answer: {answer}')


def is_on_map(antinode, dim):
    y = antinode[0]
    x = antinode[1]

    return 0 <= y < dim and 0 <= x < dim


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    antennas = []
    dim = len(lines)

    for y, line in enumerate(lines):
        for x in range(len(line.strip())):
            frequency = line[x]
            if frequency != '.':
                antennas.append((y, x, frequency))

    return antennas, dim


if __name__ == "__main__":
    main()
