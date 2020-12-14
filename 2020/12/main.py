def parse_navigation_instructions(file):
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield line[0:1], int(line[1:])


def manhattan_distance(position):
    return abs(position[0]) + abs(position[1])


def turn90(prev_orientation, prev_degrees, next_orientation):
    return next_orientation[prev_orientation], prev_degrees - 90


def turn(orientation, value, orientations_lookup):
    new_orientation = orientation
    while value > 0:
        new_orientation, value = turn90(new_orientation, value, orientations_lookup)

    return new_orientation


def right(position, orientation, _, value):
    clockwise_orientations = {
        "N": "E",
        "S": "W",
        "E": "S",
        "W": "N",
    }
    return position, turn(orientation, value, clockwise_orientations)


def left(position, orientation, _, value):
    counter_clockwise_orientations = {
        "N": "W",
        "S": "E",
        "E": "N",
        "W": "S",
    }

    return position, turn(orientation, value, counter_clockwise_orientations)


def forward(position, orientation, _, value):
    position_index = int(orientation in ["N", "S"])
    value_direction = 1 if orientation in ["N", "E"] else -1

    new_position = position.copy()
    new_position[position_index] = new_position[position_index] + value_direction * value

    return new_position, orientation


def north(position, orientation, _, value):
    return [position[0], position[1] + value], orientation


def south(position, orientation, action, value):
    return north(position, orientation, action, -1 * value)


def east(position, orientation, _, value):
    return [position[0] + value, position[1]], orientation


def west(position, orientation, action, value):
    return east(position, orientation, action, -1 * value)


def simple_navigation_final_position(navigation_instructions):
    current_position = [0, 0]
    current_orientation = "E"

    action_resolvers = {
        "N": north,
        "S": south,
        "E": east,
        "W": west,
        "L": left,
        "R": right,
        "F": forward,
    }
    for action, value in navigation_instructions:
        resolver = action_resolvers[action]
        current_position, current_orientation = resolver(current_position, current_orientation, action, value)

    return current_position


def test1():
    assert 25 == manhattan_distance(simple_navigation_final_position(parse_navigation_instructions("short_input.txt")))


def part1():
    test1()
    print(
        "Part 1: manhattan_distance",
        manhattan_distance(simple_navigation_final_position(parse_navigation_instructions("input.txt")))
    )


def waypoint_turn90(prev_degrees, waypoint):
    new_waypoint = [waypoint[1], -1 * waypoint[0]]
    return prev_degrees - 90, new_waypoint


def waypoint_turn(value, waypoint):
    new_waypoint = waypoint
    while value > 0:
        value, new_waypoint = waypoint_turn90(value, new_waypoint)

    return new_waypoint


def waypoint_right(position, value, waypoint):
    return position, waypoint_turn(value, waypoint)


def waypoint_left(position, value, waypoint):
    return position, waypoint_turn(360 - value, waypoint)


def waypoint_forward(position, value, waypoint):
    def move_coordinate(coordinate_index):
        return position[coordinate_index] + value * waypoint[coordinate_index]

    new_position = [move_coordinate(0), move_coordinate(1)]
    return new_position, waypoint


def waypoint_north(position, value, waypoint):
    return position, [waypoint[0], waypoint[1] + value]


def waypoint_south(position, value, waypoint):
    return waypoint_north(position, -1 * value, waypoint)


def waypoint_east(position, value, waypoint):
    return position, [waypoint[0] + value, waypoint[1]]


def waypoint_west(position, value, waypoint):
    return waypoint_east(position, -1 * value, waypoint)


def waypoint_navigation_final_position(navigation_instructions):
    current_position = [0, 0]
    waypoint = [10, 1]
    action_resolvers = {
        "N": waypoint_north,
        "S": waypoint_south,
        "E": waypoint_east,
        "W": waypoint_west,
        "L": waypoint_left,
        "R": waypoint_right,
        "F": waypoint_forward,
    }
    for action, value in navigation_instructions:
        resolver = action_resolvers[action]
        current_position, waypoint = resolver(current_position, value, waypoint)

    return current_position


def test2():
    assert 286 == manhattan_distance(waypoint_navigation_final_position(parse_navigation_instructions("short_input.txt")))


def part2():
    test2()
    print(
        "Part 2: manhattan_distance:",
        manhattan_distance(waypoint_navigation_final_position(parse_navigation_instructions("input.txt")))
    )


if __name__ == "__main__":
    part1()
    part2()
