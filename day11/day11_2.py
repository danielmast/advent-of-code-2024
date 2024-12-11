from collections import defaultdict

def main():
    stones = read_file('input.txt')

    counts = get_counts(stones)

    blink_count = 75
    for blink in range(blink_count):
        new_counts = defaultdict(int)
        for stone, times in counts.items():
            if stone == 0:
                new_counts[1] += times
                continue

            digit_count = len(str(stone))
            if digit_count % 2 == 0: # even number of digits
                left_stone = int(str(stone)[0:digit_count // 2])
                right_stone = int(str(stone)[digit_count // 2:digit_count])

                new_counts[left_stone] += times
                new_counts[right_stone] += times
                continue

            new_counts[stone * 2024] += times

        counts = new_counts

    answer = sum(counts.values())
    print(f'The answer: {answer}')


def get_counts(stones):
    counts = defaultdict(int)
    for stone in stones:
        counts[stone] += 1
    return counts


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    stones = [int(x) for x in lines[0].strip().split(' ')]

    return stones


if __name__ == "__main__":
    main()
