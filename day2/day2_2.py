def main():
    reports = read_file('input.txt')

    safe_count = 0

    for report in reports:
        is_valid_report, invalid_step = is_valid_report_part1(report)

        if is_valid_report:
            safe_count += 1
        else:
            alt1 = report[:invalid_step] + report[invalid_step+1:]
            alt2 = report[:invalid_step+1] + report[invalid_step+2:]

            is_valid_alt1, _ = is_valid_report_part1(alt1)
            is_valid_alt2, _ = is_valid_report_part1(alt2)

            if is_valid_alt1 or is_valid_alt2:
                safe_count += 1

    answer = safe_count
    print(f'The answer: {answer}')


def is_valid_report_part1(report):
    inc = get_inc(report)

    for i in range(len(report) - 1):
        if not is_legal_step(report[i], report[i+1], inc):
            return False, i

    return True, None


def get_inc(report):
    inc_count = 0
    for i in range(len(report) - 1):
        if report[i+1] - report[i] >= 0:
            inc_count += 1

    return inc_count > (len(report) / 2)


def is_legal_step(i1, i2, inc):
    diff = i2 - i1

    if abs(diff) < 1 or abs(diff) > 3:
        return False

    if inc and diff <= 0:
        return False

    if not inc and diff >= 0:
        return False

    return True


def read_file(input_file):
    input = open(input_file, 'r')
    lines = input.readlines()

    reports = []

    for line in lines:
        report = [int(x) for x in line.split()]
        reports.append(report)

    return reports


if __name__ == "__main__":
    main()
