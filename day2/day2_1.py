def main():
    reports = read_file('input.txt')

    safe_count = 0

    for report in reports:
        inc = (report[1] - report[0]) >= 0
        is_safe = True

        for i in range(len(report) - 1):
            diff = report[i+1] - report[i]

            if abs(diff) < 1 or abs(diff) > 3:
                is_safe = False
                break

            if inc and diff <= 0:
                is_safe = False
                break

            if not inc and diff >= 0:
                is_safe = False
                break

        if is_safe:
            safe_count += 1

    answer = safe_count
    print(f'The answer: {answer}')


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
