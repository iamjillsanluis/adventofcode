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


def test1():
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


if __name__ == "__main__":
    test1()
