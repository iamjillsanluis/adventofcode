def parse_available_adapters(file):
    data = []
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line:
                data.append(int(line))

    sorted_adapters = sorted(data)
    sorted_adapters.append(sorted_adapters[-1] + 3)  # device built-in adapter rating
    return sorted_adapters


def joltage_differences(adapters):
    current_joltage = 0

    differences = []
    for adapter in adapters:
        differences.append(adapter - current_joltage)
        current_joltage = adapter

    return differences


def product_of_joltage_differences(adapters):
    total_1_joltage, total_3_joltage = 0, 0

    for difference in joltage_differences(adapters):
        if difference == 1:
            total_1_joltage += 1
        elif difference == 3:
            total_3_joltage += 1

    return total_1_joltage * total_3_joltage


def test1():
    assert 35 == product_of_joltage_differences(parse_available_adapters("short_input.txt"))
    assert 220 == product_of_joltage_differences(parse_available_adapters("short_input2.txt"))


def part1():
    test1()
    print(
        "Part 1: joltage extreme product",
        product_of_joltage_differences(parse_available_adapters("input.txt"))
    )


if __name__ == "__main__":
    part1()
