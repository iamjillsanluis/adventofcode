def expense_report():
    result = []
    with open("input.txt") as fh:
        for line in fh:
            num = int(line.strip())
            result.append(num)
    return result


def part1(report):
    total_entries = len(report)
    answers = set()
    for first_index in range(0, total_entries):
        for second_index in range(first_index + 1, total_entries):
            first_number = report[first_index]
            second_number = report[second_index]

            if first_number + second_number == 2020:
                answers.add(first_number * second_number)
    print("Part 1:", answers)


def part2(report):
    total_entries = len(report)
    answers = set()
    for first_index in range(0, total_entries):
        for second_index in range(first_index + 1, total_entries):
            for third_index in range(second_index + 1, total_entries):
                first_number = report[first_index]
                second_number = report[second_index]
                third_number = report[third_index]

                if first_number + second_number + third_number == 2020:
                    answers.add(first_number * second_number * third_number)

    print("Part 2:", answers)


if __name__ == "__main__":
    report = expense_report()
    part1(report)
    part2(report)
