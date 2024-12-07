def main():
    assert eval([35, 20, 19], ['+', '*']) == 1045
    assert get_operators(9, 8) == ['+', '+', '+', '+', '*', '+', '+', '*']

    equations = read_file('input.txt')

    sum = 0

    for equation in equations:
        output, *inputs = equation
        operator_count = len(inputs) - 1

        for i in range(2 ** operator_count):
            operators = get_operators(i, operator_count)
            if output == eval(inputs, operators):
                sum += output
                break

    answer = sum
    print(f'The answer: {answer}')


def get_operators(i, operator_count):
    binary = bin(i)[2:].zfill(operator_count)

    ops = ['+', '*']

    combination = []
    for b in binary:
        combination.append(ops[int(b)])

    return combination


def eval(inputs, operators):
    if len(inputs) != len(operators) + 1:
        assert False

    outcome = inputs[0]

    for i in range(0, len(operators)):
        if operators[i] == '+':
            outcome += inputs[i+1]
        else:
            outcome *= inputs[i+1]

    return outcome


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    equations = []

    for line in lines:
        output = int(line.split(':')[0])
        inputs = [int(x) for x in line.split(':')[1].split()]
        equation = [output] + inputs
        equations.append(equation)

    return equations


if __name__ == "__main__":
    main()
