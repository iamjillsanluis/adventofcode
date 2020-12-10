def parse_adapter_joltage_ratings(file):
    data = []
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line:
                data.append(int(line))

    return data


def product_of_joltage_differences(adapters):
    sorted_adapters = sorted(adapters)
    sorted_adapters.append(sorted_adapters[-1] + 3)  # device built-in adapter rating

    current_joltage = 0
    total_1_joltage, total_3_joltage = 0, 0

    for adapter in sorted_adapters:
        joltage_difference = adapter - current_joltage
        if joltage_difference == 1:
            total_1_joltage += 1
        elif joltage_difference == 3:
            total_3_joltage += 1

        current_joltage = adapter

    return total_1_joltage * total_3_joltage


def test1():
    assert 35 == product_of_joltage_differences(parse_adapter_joltage_ratings("short_input.txt"))
    assert 220 == product_of_joltage_differences(parse_adapter_joltage_ratings("short_input2.txt"))


def part1():
    test1()
    print(
        "Part 1: joltage extreme product",
        product_of_joltage_differences(parse_adapter_joltage_ratings("input.txt"))
    )


if __name__ == "__main__":
    part1()
