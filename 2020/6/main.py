from collections import defaultdict


def groups_yes_responses(file):
    group_responses = []
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line == "":
                yield group_responses
                group_responses = []
            else:
                group_responses.append(line)

    if group_responses:
        yield group_responses


def sum_of_unique_group_responses_count(file):
    result = 0
    for group_responses in groups_yes_responses(file):
        unique_group_responses = set()
        for person_yes_responses in group_responses:
            for yes in person_yes_responses:
                unique_group_responses.add(yes)

        result += len(unique_group_responses)

    return result


def test1():
    assert 11 == sum_of_unique_group_responses_count("test.txt")


def part1():
    print("Part 1: sum", sum_of_unique_group_responses_count("input.txt"))


def sum_of_aligned_group_responses_count(file):
    result = 0
    for group_responses in groups_yes_responses(file):
        yeses = defaultdict(int)
        for person_yes_responses in group_responses:
            for question in person_yes_responses:
                yeses[question] += 1

        for question in yeses:
            if yeses[question] == len(group_responses):
                result += 1
    return result


def test2():
    assert 6 == sum_of_aligned_group_responses_count("test.txt")


def part2():
    print("Part 2: sum", sum_of_aligned_group_responses_count("input.txt"))


if __name__ == "__main__":
    test1()
    part1()
    test2()
    part2()
