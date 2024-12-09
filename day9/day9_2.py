from collections import namedtuple

File = namedtuple('File', ['id', 'size'])


def main():
    test_map = '2333133121414131402'
    assert ''.join(expand(rearrange(map_to_list(test_map)))) == '00992111777.44.333....5555.6666.....8888..'
    assert get_checksum(expand(rearrange(map_to_list(test_map)))) == 2858

    map = read_file('input.txt')
    map_list = map_to_list(map)
    rearranged = rearrange(map_list)
    expanded = expand(rearranged)
    checksum = get_checksum(expanded)

    print(f'The answer: {checksum}')


def map_to_list(map):
    list_map = []

    for i, m in enumerate(map):
        size = int(m)
        if i % 2 == 0:
            id = i // 2
        else:
            id = '.'
        list_map.append(File(id=id, size=size))

    return list_map


def rearrange(map_list):
    rearranged = map_list.copy()

    i_right = len(rearranged) - 1
    while i_right >= 0:
        right_file = rearranged[i_right]
        if right_file.id != '.':
            for i_left in range(0, i_right):
                left_file = rearranged[i_left]
                if left_file.id == '.' and left_file.size >= right_file.size:
                    rearranged[i_left] = right_file
                    rearranged[i_right] = File(id='.', size=right_file.size)

                    diff = left_file.size - right_file.size
                    if diff > 0:
                        rearranged.insert(i_left + 1, File(id='.', size=diff))
                    break
        i_right -= 1

    return rearranged


def expand(rearranged):
    expanded = []

    for file in rearranged:
        expanded += [str(file.id)] * file.size

    return expanded


def get_checksum(rearranged):
    sum = 0

    for i, r in enumerate(rearranged):
        if r != '.':
            sum += i * int(r)

    return sum


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines[0].strip()


if __name__ == "__main__":
    main()
