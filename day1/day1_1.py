def main():
    left, right = read_file('input.txt')

    left.sort()
    right.sort()

    sum = 0

    for i in range(len(left)):
        sum += abs(left[i] - right[i])

    answer = sum
    print(f'The answer: {answer}')


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    left = []
    right = []

    for line in lines:
        l, r = [int(x) for x in line.split()]
        left.append(l)
        right.append(r)

    return left, right


if __name__ == "__main__":
    main()
