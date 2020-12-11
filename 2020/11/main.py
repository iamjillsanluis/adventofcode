def parse_layout(file):
    layout = []

    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line:
                layout.append(list(line.strip()))
    return layout


def within_layout(row_index, col_index, layout_length, layout_width):
    return 0 <= row_index < layout_length and 0 <= col_index < layout_width


def total_adjacent_occupied_seats_myopic(layout, row_index, col_index):
    length = len(layout)
    width = len(layout[0])

    steps = [
        [row_step, col_step]
        for row_step in [-1, 0, 1]
        for col_step in [-1, 0, 1]
    ]

    counter = 0
    for row_step, col_step in steps:
        adj_row_index = row_step + row_index
        adj_col_index = col_step + col_index

        if (within_layout(adj_row_index, adj_col_index, length, width)
            and not (row_index == adj_row_index and col_index == adj_col_index)
            and layout[adj_row_index][adj_col_index] == "#"
        ):
            counter += 1

    return counter


def total_adjacent_occupied_seats_2020(layout, row_index, col_index):
    length = len(layout)
    width = len(layout[0])

    steps = [
        [row_step, col_step]
        for row_step in [-1, 0, 1]
        for col_step in [-1, 0, 1]
    ]

    counter = 0
    for row_step, col_step in steps:
        if row_step == col_step == 0:
            continue

        adj_row_index = row_step + row_index
        adj_col_index = col_step + col_index
        while within_layout(adj_row_index, adj_col_index, length, width):
            if layout[adj_row_index][adj_col_index] == "#":
                counter += 1

            if layout[adj_row_index][adj_col_index] != ".":
                break

            adj_row_index += row_step
            adj_col_index += col_step

    return counter


def resolve_new_layout(original_layout, occupied_adjacent_seats_counter, social_tolerance):
    new_layout = [
        row.copy()
        for row in original_layout
    ]

    length = len(new_layout)
    width = len(new_layout[0])
    for row_index in range(0, length):
        for col_index in range(0, width):
            current_position = original_layout[row_index][col_index]

            if current_position == ".":
                continue

            total_occupied_adjacent_seats = occupied_adjacent_seats_counter(original_layout, row_index, col_index)

            if current_position == "L" and total_occupied_adjacent_seats == 0:
                new_layout[row_index][col_index] = "#"
            elif current_position == "#" and total_occupied_adjacent_seats >= social_tolerance:
                new_layout[row_index][col_index] = "L"

    return new_layout


def total_occupied_seats_on_stabilization(layout, occupied_adjacent_seats_counter, social_tolerance):
    next_layout = resolve_new_layout(layout, occupied_adjacent_seats_counter, social_tolerance)

    while layout != next_layout:
        layout = next_layout
        next_layout = resolve_new_layout(layout, occupied_adjacent_seats_counter, social_tolerance)

    total_occupied_seats = 0
    for row in layout:
        for seat in row:
            if seat == "#":
                total_occupied_seats += 1
    return total_occupied_seats


def test1():
    assert parse_layout("example_p1_2.txt") == resolve_new_layout(
        original_layout=parse_layout("example.txt"),
        occupied_adjacent_seats_counter=total_adjacent_occupied_seats_myopic,
        social_tolerance=4
    )
    assert 37 == total_occupied_seats_on_stabilization(
        layout=parse_layout("example.txt"),
        occupied_adjacent_seats_counter=total_adjacent_occupied_seats_myopic,
        social_tolerance=4
    )


def part1():
    test1()
    print(
        "Part 1: total occupied seats",
        total_occupied_seats_on_stabilization(
            layout=parse_layout("input.txt"),
            occupied_adjacent_seats_counter=total_adjacent_occupied_seats_myopic,
            social_tolerance=4
        )
    )


def test2():
    assert 8 == total_adjacent_occupied_seats_2020(layout=parse_layout("2020_example_1.txt"), row_index=4, col_index=3)
    assert 0 == total_adjacent_occupied_seats_2020(layout=parse_layout("2020_example_2.txt"), row_index=1, col_index=1)
    assert 1 == total_adjacent_occupied_seats_2020(layout=parse_layout("2020_example_2.txt"), row_index=1, col_index=3)
    assert 0 == total_adjacent_occupied_seats_2020(layout=parse_layout("2020_example_3.txt"), row_index=3, col_index=3)
    assert parse_layout("example_p2_2.txt") == resolve_new_layout(
        original_layout=parse_layout("example.txt"),
        occupied_adjacent_seats_counter=total_adjacent_occupied_seats_2020,
        social_tolerance=5
    )
    assert 26 == total_occupied_seats_on_stabilization(
        layout=parse_layout("example.txt"),
        occupied_adjacent_seats_counter=total_adjacent_occupied_seats_2020,
        social_tolerance=5
    )


def part2():
    test2()
    print(
        "Part 2: total occupied seats",
        total_occupied_seats_on_stabilization(
            layout=parse_layout("input.txt"),
            occupied_adjacent_seats_counter=total_adjacent_occupied_seats_2020,
            social_tolerance=5
        )
    )


if __name__ == "__main__":
    part1()
    part2()
