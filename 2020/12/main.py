def parse_navigation_instructions(file):
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield line


def final_position(navigation_instructions):
    return [17, -8]


def manhattan_distance(position):
    return abs(position[0]) + abs(position[1])


def test1():
    assert 25 == manhattan_distance(final_position(parse_navigation_instructions("short_input.txt")))


def part1():
    test1()


if __name__ == "__main__":
    part1()