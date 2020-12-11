def parse_layout(file):
    layout = []

    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line:
                layout.append(list(line.strip()))
    return layout


def adjacent_seats_boundaries(value, max_value):
    if value == 0:
        return [0, 1]
    elif value == max_value - 1:
        return [value-1, value]
    else:
        return [value-1, value, value+1]


def adjacent_seats_positions(row_index, col_index, length, width):
    row_boundaries = adjacent_seats_boundaries(row_index, length)
    col_boundaries = adjacent_seats_boundaries(col_index, width)

    for adj_row_index in row_boundaries:
        for adj_col_index in col_boundaries:
            if not (adj_row_index == row_index and adj_col_index == col_index):
                yield adj_row_index, adj_col_index


def resolve_new_layout(original_layout):
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

            total_occupied_adjacent_seats = len([
                True
                for adj_row_index, adj_column_index in adjacent_seats_positions(row_index, col_index, length, width)
                if original_layout[adj_row_index][adj_column_index] == "#"
            ])

            if current_position == "L" and total_occupied_adjacent_seats == 0:
                new_layout[row_index][col_index] = "#"
            elif current_position == "#" and total_occupied_adjacent_seats >= 4:
                new_layout[row_index][col_index] = "L"

    return new_layout


def total_occupied_seats_on_stabilization(layout):
    next_layout = resolve_new_layout(layout)

    while layout != next_layout:
        layout = next_layout
        next_layout = resolve_new_layout(layout)

    total_occupied_seats = 0
    for row in layout:
        for seat in row:
            if seat == "#":
                total_occupied_seats += 1
    return total_occupied_seats


def test1():
    assert parse_layout("example_2.txt") == resolve_new_layout(parse_layout("example.txt"))
    assert 37 == total_occupied_seats_on_stabilization(parse_layout("example.txt"))


def part1():
    test1()


if __name__ == "__main__":
    part1()
