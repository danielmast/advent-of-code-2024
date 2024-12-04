

def main():
    input = read_file('input.txt')
    print(f'The answer: {solve(input)}')


chunks = [0, 0]


def solve(input):
    global chunks

    n = len(input)
    sum = 0

    # Horizontal
    for y in range(0, n):
        for x in range(0, n):
            sum += process_letter(y, x, input, 'XMAS', 0)
            sum += process_letter(y, x, input, 'SAMX', 1)

        chunks = [0, 0]


    # Vertical
    for x in range(0, n):
        for y in range(0, n):
            sum += process_letter(y, x, input, 'XMAS', 0)
            sum += process_letter(y, x, input, 'SAMX', 1)

        chunks = [0, 0]


    # Diagonal (\)
    for d in range(0, 2*n - 1):
        for i in range(0, n):
            x = -1
            y = -1
            if d < n:
                y = n - d - 1 + i
                x = i
            else:
                y = i
                x = d - n + i + 1

            if x < 0 or x >= n or y < 0 or y >= n:
                break

            sum += process_letter(y, x, input, 'XMAS', 0)
            sum += process_letter(y, x, input, 'SAMX', 1)

        chunks = [0, 0]


    # Diagonal (/)
    for d in range(0, 2*n - 1):
        for i in range(0, n):
            x = -1
            y = -1
            if d < n:
                y = d - i
                x = 0 + i
            else:
                y = n - 1 - i
                x = d - n + 1 + i

            if x < 0 or x >= n or y < 0 or y >= n:
                break

            sum += process_letter(y, x, input, 'XMAS', 0)
            sum += process_letter(y, x, input, 'SAMX', 1)

        chunks = [0, 0]

    return sum


def process_letter(y, x, input, word, chunk):
    global chunks

    letter = input[y][x]

    try:
        word.index(letter)
    except ValueError:
        return 0

    if chunks[chunk] == word.index(letter):
        chunks[chunk] += 1

        if chunks[chunk] == len(word):
            chunks[chunk] = 0
            return 1
    elif letter == word[0]:
        chunks[chunk] = 1
    else:
        chunks[chunk] = 0

    return 0


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    result = []

    for line in lines:
        result.append(line.strip())

    return result


if __name__ == "__main__":
    main()
