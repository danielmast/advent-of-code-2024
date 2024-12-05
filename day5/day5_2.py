def main():
    rules, updates = read_file('input.txt')

    sum = 0

    for update in updates:
        if not is_legal_update(update, rules):
            sum += middle_page(make_legal(update, rules))

    answer = sum
    print(f'The answer: {answer}')


def make_legal(update, rules):
    legal = []

    for page in update:
        min_i = 0
        max_i = len(legal)
        for rule in rules:
            if rule[0] == page and rule[1] in legal:
                max_i = min(max_i, legal.index(rule[1]))
            elif rule[0] in legal and rule[1] == page:
                min_i = max(min_i, legal.index(rule[0]) + 1)

            if min_i == max_i:
                legal.insert(min_i, page)
                break

    return legal


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

    reading_rules = True

    for line in lines:
        line = line.strip()

        if line == '':
            reading_rules = False
            continue

        if reading_rules:
            rule = [int(x) for x in line.split('|')]
            rules.append(rule)
        else:
            update = [int(x) for x in line.split(',')]
            updates.append(update)

    return rules, updates


if __name__ == "__main__":
    main()
