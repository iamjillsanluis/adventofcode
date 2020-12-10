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

    for adapter in adapters:
        yield adapter - current_joltage
        current_joltage = adapter


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


def total_arrangements_for_ones_chain(chain_len):
    if chain_len <= 1:
        return 1

    result = 2**(chain_len-1)
    if chain_len - 3 > 0:
        result -= 2**(chain_len - 3) - 1
    return result


def distinct_adapter_arrangements(adapters):
    distinct_arrangements = 1
    start_index = None
    for index, difference in enumerate(joltage_differences(adapters)):
        if difference == 3 and start_index is not None:
            distinct_arrangements *= total_arrangements_for_ones_chain(index - start_index)
            start_index = None

        if start_index is None and difference == 1:
            start_index = index

    return distinct_arrangements


def test2():
    assert 8 == distinct_adapter_arrangements(parse_available_adapters("short_input.txt"))
    assert 19208 == distinct_adapter_arrangements(parse_available_adapters("short_input2.txt"))


def part2():
    test2()
    print("Part 2: distinct arrangements:", distinct_adapter_arrangements(parse_available_adapters("input.txt")))


if __name__ == "__main__":
    part1()
    part2()
