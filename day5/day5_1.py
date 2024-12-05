def main():
    rules, updates = read_file('input.txt')

    sum = 0

    for update in updates:
        if is_legal_update(update, rules):
            sum += middle_page(update)

    answer = sum
    print(f'The answer: {answer}')


def is_legal_update(update, rules):
    illegal = set()

    for page in update:
        if page in illegal:
            return False

        for rule in rules:
            if rule[1] == page:
                illegal.add(rule[0])

    return True


def middle_page(update):
    return update[int((len(update) - 1) / 2)]


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    rules = []
    updates = []

    is_reading_rules = True

    for line in lines:
        line = line.strip()

        if line == '':
            is_reading_rules = False
            continue

        if is_reading_rules:
            rule = [int(x) for x in line.split('|')]
            rules.append(rule)
        else:
            update = [int(x) for x in line.split(',')]
            updates.append(update)

    return rules, updates


if __name__ == "__main__":
    main()
