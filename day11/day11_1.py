def main():
    stones = read_file('input.txt')

    blink_count = 25
    for blink in range(blink_count):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
                continue

            digit_count = len(str(stone))
            if digit_count % 2 == 0: # even number of digits
                new_stones.append(int(str(stone)[0:digit_count // 2]))
                new_stones.append(int(str(stone)[digit_count // 2:digit_count]))
                continue

            new_stones.append(stone * 2024)
        stones = new_stones

    answer = len(stones)
    print(f'The answer: {answer}')


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    stones = [int(x) for x in lines[0].strip().split(' ')]

    return stones


if __name__ == "__main__":
    main()
