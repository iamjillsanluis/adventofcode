def parse_navigation_instructions(file):
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield line[0:1], int(line[1:])


def north(position, orientation, _, value):
    return [position[0], position[1] + value], orientation


def south(position, orientation, action, value):
    return north(position, orientation, action, -1 * value)


def east(position, orientation, _, value):
    return [position[0] + value, position[1]], orientation


def west(position, orientation, action, value):
    return east(position, orientation, action, -1 * value)


def turn90(prev_orientation, prev_degrees, next_orientation):
    return next_orientation[prev_orientation], prev_degrees - 90


def turn(orientation, value, orientations_lookup):
    new_orientation = orientation
    while value > 0:
        new_orientation, value = turn90(new_orientation, value, orientations_lookup)

    return new_orientation


def right(position, orientation, _, value):
    orientations_lookup = {
        "N": "E",
        "S": "W",
        "E": "S",
        "W": "N",
    }
    return position, turn(orientation, value, orientations_lookup)


def left(position, orientation, _, value):
    orientations_lookup = {
        "N": "W",
        "S": "E",
        "E": "N",
        "W": "S",
    }
    return position, turn(orientation, value, orientations_lookup)


def forward(position, orientation, _, value):
    position_index = int(orientation in ["N", "S"])
    value_direction = 1 if orientation in ["N", "E"] else -1

    new_position = position.copy()
    new_position[position_index] = new_position[position_index] + value_direction * value

    return new_position, orientation


def final_position(navigation_instructions):
    current_position = [0, 0]
    current_orientation = "E"
    for action, value in navigation_instructions:
        current_position, current_orientation = {
            "N": north,
            "S": south,
            "E": east,
            "W": west,
            "L": left,
            "R": right,
            "F": forward,
        }[action](current_position, current_orientation, action, value)

    return current_position


def manhattan_distance(position):
    return abs(position[0]) + abs(position[1])


def test1():
    assert 25 == manhattan_distance(final_position(parse_navigation_instructions("short_input.txt")))


def part1():
    test1()
    print(
        "Part 1: manhattan_distance",
        manhattan_distance(final_position(parse_navigation_instructions("input.txt")))
    )


if __name__ == "__main__":
    part1()
