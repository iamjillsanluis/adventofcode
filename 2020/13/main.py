import sys


def parse_input(file):
    with open(file) as fh:
        lines = [line.strip() for line in fh]

        optimal_departure_time = int(lines[0])
        bus_ids = [
            int(bus_id)
            for bus_id in lines[1].split(",")
            if bus_id != "x"
        ]

        return optimal_departure_time, bus_ids


def earliest_bus_solution(file):
    optimal_departure_time, bus_ids = parse_input(file)
    buses_departures = [
        (bus_id, int(optimal_departure_time / bus_id), optimal_departure_time % bus_id)
        for bus_id in bus_ids
    ]

    wait_time = sys.maxsize
    bus = None
    for bus_id, bus_round, mins_before_departure_time in buses_departures:
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


if __name__ == "__main__":
    part1()
