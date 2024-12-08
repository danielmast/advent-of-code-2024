from collections import namedtuple


def main():
    antennas, dim = read_file('input.txt')

    antinodes = set()
    Antinode = namedtuple('Antinode', ['y', 'x'])

    for i in range(len(antennas)):
        for j in range(len(antennas)):
            antenna1 = antennas[i]
            antenna2 = antennas[j]

            if antenna1 == antenna2 or antenna1.frequency != antenna2.frequency:
                continue

            diff_y = antenna1.y - antenna2.y
            diff_x = antenna1.x - antenna2.x

            antinodes.add(Antinode(y=antenna1.y, x=antenna1.x))

            next_antinode = Antinode(y=antenna1.y + diff_y, x=antenna1.x + diff_x)

            while is_on_map(next_antinode, dim):
                antinodes.add(next_antinode)
                next_antinode = Antinode(y=next_antinode.y + diff_y, x=next_antinode.x + diff_x)

            next_antinode = Antinode(y=antenna1.y - diff_y, x=antenna1.x - diff_x)

            while is_on_map(next_antinode, dim):
                antinodes.add(next_antinode)
                next_antinode = Antinode(next_antinode.y - diff_y, next_antinode.x - diff_x)

    answer = len(antinodes)
    print(f'The answer: {answer}')


def is_on_map(antinode, dim):
    return 0 <= antinode.y < dim and 0 <= antinode.x < dim


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    antennas = []
    dim = len(lines)

    Antenna = namedtuple('Antenna', ['y', 'x', 'frequency'])

    for y, line in enumerate(lines):
        for x in range(len(line.strip())):
            frequency = line[x]
            if frequency != '.':
                antennas.append(Antenna(y, x, frequency))

    return antennas, dim


if __name__ == "__main__":
    main()
