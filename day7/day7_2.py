def main():
    assert eval([35, 20, 19], ['+', '*']) == 1045
    assert eval([6, 8, 6, 15], ['*', '||', '*']) == 7290

    assert decimal_to_3ary(8, 2) == '22'
    assert decimal_to_3ary(9, 4) == '0100'
    assert decimal_to_3ary(35, 6) == '001022'

    assert get_operators(8, 2) == ['||', '||']
    assert get_operators(35, 6) == ['+', '+', '*', '+', '||', '||']

    equations = read_file('input.txt')

    sum = 0

    for e, equation in enumerate(equations):
        output, *inputs = equation
        operator_count = len(inputs) - 1

        for i in range(3 ** operator_count):
            operators = get_operators(i, operator_count)
            if output == eval(inputs, operators):
                sum += output
                break

    answer = sum
    print(f'The answer: {answer}')


def get_operators(i, operator_count):
    three_ary = decimal_to_3ary(i, operator_count)

    ops = ['+', '*', '||']

    combination = []
    for t in three_ary:
        combination.append(ops[int(t)])

    return combination


def decimal_to_3ary(d, n):
    three_ary = ''
    rest = d

    for i in range(n-1, -1, -1):
        times = rest // 3**i
        three_ary += str(times)
        rest -= times * 3**i

    return three_ary.zfill(n)


def eval(inputs, operators):
    if len(inputs) != len(operators) + 1:
        assert False

    outcome = inputs[0]

    for i in range(0, len(operators)):
        if operators[i] == '+':
            outcome += inputs[i+1]
        elif operators[i] == '*':
            outcome *= inputs[i+1]
        else:
            outcome = int(str(outcome) + str(inputs[i+1]))

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
