def parse_partial_terrain():
    result = []
    with open("input.txt") as fh:
        for line in fh:
            result.append(line.strip())
    return result


def count_trees_encountered(partial_terrain, right, down):
    terrain = full_terrain(partial_terrain, right, down)

    total_count = 0
    width, height = len(terrain[0]), len(terrain)
    x_pos, y_pos = 0, 0
    while x_pos < width and y_pos < height:
        if terrain[y_pos] and terrain[y_pos][x_pos] and terrain[y_pos][x_pos] == "#":
            total_count += 1

        x_pos += right
        y_pos += down

    return total_count


def full_terrain(partial_terrain, right, down):
    height = len(partial_terrain)
    initial_width = len(partial_terrain[0])
    terrain = []
    factor = int(right * height / down / initial_width) + 1
    for row in partial_terrain:
        terrain.append(row*factor)

    return terrain


def part1():
    print("Part 1: Total trees encountered", count_trees_encountered(parse_partial_terrain(), right=3, down=1))


def part2():
    product = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        product *= count_trees_encountered(parse_partial_terrain(), right, down)
    print("Part 2: Final product", product)


if __name__ == "__main__":
    part1()
    part2()
