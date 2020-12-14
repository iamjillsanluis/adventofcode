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


def earliest_departure_timestamp(bus_schedules, start_timestamp=None):
    bus_departure_offsets = {
        int(bus_id): offset
        for offset, bus_id in enumerate(bus_schedules)
        if bus_id != "x"
    }

    reference_bus = max(bus_id for bus_id in bus_departure_offsets)
    reference_bus_offset = bus_departure_offsets[reference_bus]

    constraints = [
        (bus_id, offset - reference_bus_offset)
        for bus_id, offset in bus_departure_offsets.items()
        if bus_id != reference_bus
    ]

    iteration = int((start_timestamp or reference_bus) / reference_bus)
    while True:
        reference_bus_timestamp = reference_bus * iteration
        found = True
        for bus_id, offset in constraints:
            if (reference_bus_timestamp + offset) % bus_id > 0:
                found = False
                break

        if found:
            print(f"{iteration} timestamp: {reference_bus_timestamp}")
            return reference_bus_timestamp - reference_bus_offset

        if iteration % 1000000 == 0:
            print(f"checkpoint: {iteration} timestamp: {reference_bus_timestamp}")

        iteration += 1


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
