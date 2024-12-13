import re
from sympy import symbols, Eq, solve, Integer


def main():
    machines = read_file('input.txt')
    answer = sum([fewest_tokens(machine) for machine in machines])
    print(f'The answer: {answer}')


def fewest_tokens(machine):
    a, b = symbols('a b')

    eq1 = Eq(machine.button_a.y * a + machine.button_b.y * b, machine.prize.y)
    eq2 = Eq(machine.button_a.x * a + machine.button_b.x * b, machine.prize.x)

    solution = solve((eq1, eq2), (a, b))

    if isinstance(solution[a], Integer):
        return cost(int(solution[a]), int(solution[b]))
    else:
        return 0


def cost(button_a_presses, button_b_presses):
    return 3 * button_a_presses + button_b_presses


class Machine:
    def __init__(self, button_a, button_b, prize):
        self.button_a = button_a
        self.button_b = button_b
        self.prize = prize

    def __str__(self):
        return f'Machine: {self.button_a}, {self.button_b}, {self.prize}'


class Button:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def __str__(self):
        return f'Button {self.id}: X+{self.x}, Y+{self.y}'


class Prize:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Prize: X={self.x}, Y={self.y}'


def read_file(input_file):
    input = open(input_file, 'r')
    lines = [line.strip() for line in input.readlines()]

    machines = []
    button_a = button_b = None

    for line in lines:
        if line.startswith('Button'):
            matches = re.match(r"Button ([A-B]): X\+([0-9]+), Y\+([0-9]+)", line).groups(0)
            id = matches[0]
            x = int(matches[1])
            y = int(matches[2])

            if id == 'A':
                button_a = Button(id, x, y)
            else:
                button_b = Button(id, x, y)
        elif line.startswith('Prize'):
            matches = re.match(r"Prize: X=([0-9]+), Y=([0-9]+)", line).groups(0)
            x = int(matches[0]) + 10000000000000
            y = int(matches[1]) + 10000000000000
            prize = Prize(x, y)
            machine = Machine(button_a, button_b, prize)
            machines.append(machine)
        else:
            button_a = button_b = None

    return machines


if __name__ == "__main__":
    main()
