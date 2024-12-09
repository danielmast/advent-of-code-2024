
def main():
    test_map = '2333133121414131402'
    assert ''.join(expand(test_map)) == '00...111...2...333.44.5555.6666.777.888899'
    assert ''.join(rearrange(expand(test_map))) == '0099811188827773336446555566..............'
    assert get_checksum(rearrange(expand(test_map))) == 1928

    map = read_file('input.txt')

    expanded = expand(map)
    rearranged = rearrange(expanded)
    checksum = get_checksum(rearranged)

    print(f'The answer: {checksum}')


def expand(map):
    expanded = []

    for i, m in enumerate(map):
        if i % 2 == 0: # even -> disk
            expanded += [str(i // 2)] * int(m)
        else: # odd -> free
            expanded += ['.'] * int(m)

    return expanded


def rearrange(expanded):
    rearranged = expanded.copy()
    i_left = 0
    i_right = len(expanded) - 1

    while i_left < i_right:
        if rearranged[i_left] != '.':
            i_left += 1
            continue
        elif rearranged[i_right] == '.':
            i_right -= 1
            continue

        rearranged[i_left] = rearranged[i_right]
        rearranged[i_right] = '.'
        i_left += 1
        i_right -= 1

    return rearranged


def get_checksum(rearranged):
    sum = 0

    for i, r in enumerate(rearranged):
        if r == '.':
            return sum

        sum += i * int(r)


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    return lines[0].strip()


if __name__ == "__main__":
    main()
