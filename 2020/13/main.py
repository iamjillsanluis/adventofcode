import sys


def parse_input(file):
    with open(file) as fh:
        lines = [line.strip() for line in fh]

        optimal_departure_time = int(lines[0])
        bus_ids = [
            bus_id
            for bus_id in lines[1].split(",")
        ]

        return optimal_departure_time, bus_ids


def buses_departures(bus_ids, optimal_departure_time):
    return [
        (bus_id, int(optimal_departure_time / bus_id), optimal_departure_time % bus_id)
        for bus_id in [int(b) for b in bus_ids if b != "x"]
    ]


def earliest_bus_solution(file):
    optimal_departure_time, bus_ids = parse_input(file)

    wait_time = sys.maxsize
    bus = None
    for bus_id, bus_round, mins_before_departure_time in buses_departures(bus_ids, optimal_departure_time):
        if mins_before_departure_time == 0:
            return 0
        else:
            bus_wait_time = ((bus_round + 1) * bus_id) - optimal_departure_time

        if bus_wait_time < wait_time:
            wait_time = bus_wait_time
            bus = bus_id

        wait_time = min(bus_wait_time, wait_time)

    return wait_time * bus


def test1():
    assert 295 == earliest_bus_solution("short_input.txt")


def part1():
    test1()
    print("Part 1: solution", earliest_bus_solution("input.txt"))


def earliest_departure_timestamp(buses, start_timestamp=None):
    first_bus_id = int(buses[0])

    step = first_bus_id
    earliest_timestamp = first_bus_id if start_timestamp is None else start_timestamp - (start_timestamp % step)

    for bus_offset in range(1, len(buses)):
        bus_id = buses[bus_offset]
        if bus_id != "x":
            bus_id = int(bus_id)
            while True:
                if (earliest_timestamp + bus_offset) % bus_id == 0:
                    break
                earliest_timestamp += step
            step *= bus_id

    return earliest_timestamp


def test2():
    assert 3417 == earliest_departure_timestamp([17, "x", 13, 19])
    assert 754018 == earliest_departure_timestamp([67, 7, 59, 61])
    assert 779210 == earliest_departure_timestamp([67, "x", 7, 59, 61])
    assert 1261476 == earliest_departure_timestamp([67, 7, "x", 59, 61])
    assert 1202161486 == earliest_departure_timestamp([1789, 37, 47, 1889])
    assert 1068781 == earliest_departure_timestamp([7, 13, "x", "x", 59, "x", 31, 19])


def part2():
    test2()
    _, bus_ids = parse_input("input.txt")
    print("Part 2: solution", earliest_departure_timestamp(bus_ids, start_timestamp=100000000000000))


if __name__ == "__main__":
    part1()
    part2()
