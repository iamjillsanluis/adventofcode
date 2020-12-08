import re


def parse_rules(file):
    rules = {}
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            outer_bag, raw_inner_bags = line.split(" bags contain ")

            rules[outer_bag] = {}
            for match in re.findall(r"((\d+) ([a-z ]+) bags?)+", raw_inner_bags):
                rules[outer_bag][match[2]] = int(match[1])
    return rules


def test_parse_rules():
    expected = {
        "light red": {"bright white": 1, "muted yellow": 2},
        "dark orange": {"bright white": 3, "muted yellow": 4},
        "bright white": {"shiny gold": 1},
        "muted yellow": {"shiny gold": 2, "faded blue": 9},
        "shiny gold": {"dark olive": 1, "vibrant plum": 2},
        "dark olive": {"faded blue": 3, "dotted black": 4},
        "vibrant plum": {"faded blue": 5, "dotted black": 6},
        "faded blue": {},
        "dotted black": {}
    }
    actual = parse_rules("short_input.txt")
    assert expected == actual


def can_hold_shiny_gold_bag(outer_bag, rules):
    if not rules:
        return False

    if rules[outer_bag].get("shiny gold", 0) > 0:
        return True

    for outer_bag_candidate in rules[outer_bag]:
        if can_hold_shiny_gold_bag(outer_bag_candidate, rules):
            return True

    return False


def count_shiny_gold_bag_outer_bags(file):
    count = 0
    rules = parse_rules(file)
    for outer_bag in rules:
        if can_hold_shiny_gold_bag(outer_bag, rules):
            count += 1
    return count


def test_count_shiny_gold_bag_outer_bags():
    assert 4 == count_shiny_gold_bag_outer_bags("short_input.txt")


def part1():
    count = count_shiny_gold_bag_outer_bags("input.txt")
    print("Part 1: Total outer bags that can hold shiny gold bag", count)


if __name__ == "__main__":
    test_parse_rules()
    test_count_shiny_gold_bag_outer_bags()
    part1()

