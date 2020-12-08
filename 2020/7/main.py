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


def total_shiny_gold_bag_outer_bags(file):
    total = 0
    rules = parse_rules(file)
    for outer_bag in rules:
        if can_hold_shiny_gold_bag(outer_bag, rules):
            total += 1
    return total


def test_total_shiny_gold_bag_outer_bags():
    assert 4 == total_shiny_gold_bag_outer_bags("short_input.txt")


def part1():
    total = total_shiny_gold_bag_outer_bags("input.txt")
    print("Part 1: Total outer bags that can hold shiny gold bag", total)


def total_bags_within(bag, rules):
    bag_rule = rules.get(bag, {})
    if not bag_rule:
        return 0

    total = 0
    for inner_bag, inner_bag_total in bag_rule.items():
        total += inner_bag_total + (inner_bag_total * total_bags_within(inner_bag, rules))
    return total


def total_individual_bags_inside_shiny_gold_bag(file):
    rules = parse_rules(file)
    return total_bags_within("shiny gold", rules)


def test_total_individual_bags_inside_shiny_gold_bag():
    assert 32 == total_individual_bags_inside_shiny_gold_bag("short_input.txt")
    assert 126 == total_individual_bags_inside_shiny_gold_bag("short_input2.txt")


def part2():
    total = total_individual_bags_inside_shiny_gold_bag("input.txt")
    print("Part 2: Total individual bags within shiny gold bag", total)


if __name__ == "__main__":
    test_parse_rules()
    test_total_shiny_gold_bag_outer_bags()
    part1()

    test_total_individual_bags_inside_shiny_gold_bag()
    part2()
