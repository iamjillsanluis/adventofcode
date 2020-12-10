def data_feed(file):
    data = []
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line:
                data.append(int(line))

    return data


def has_no_summing_pairs(data, pre_amble_size, candidate_index):
    pre_amble = data[candidate_index - pre_amble_size:candidate_index]
    target_sum = data[candidate_index]

    for augend_index, augend in enumerate(pre_amble[:-1]):
        for addend in pre_amble[augend_index + 1:]:
            if augend + addend == target_sum:
                return False
    return True


def find_corrupted_entry(data, pre_amble_size):
    candidates = [
        data[candidate_index]
        for candidate_index in range(pre_amble_size, len(data))
        if has_no_summing_pairs(data, pre_amble_size, candidate_index)
    ]

    return candidates[0] if len(candidates) == 1 else None


def find_contiguous_range_min_max_sum(data, target_sum):
    index_of_target = data.index(target_sum)
    for start_index in range(0, index_of_target):
        running_sum = 0
        running_index = start_index
        while running_sum < target_sum and running_index < index_of_target:
            running_sum += data[running_index]
            running_index += 1

        if running_sum == target_sum:
            sorted_range = sorted(data[start_index:running_index])
            return sorted_range[0] + sorted_range[-1]

    return []


def test1():
    assert 127 == find_corrupted_entry(data_feed("short_input.txt"), 5)


def part1():
    test1()
    result = find_corrupted_entry(data_feed("input.txt"), 25)
    assert 22477624 == result
    print("Part 1: corrupted entry:", result)


def test2():
    assert 62 == find_contiguous_range_min_max_sum(data_feed("short_input.txt"), 127)


def part2():
    test2()
    data = data_feed("input.txt")
    result = find_contiguous_range_min_max_sum(data,  target_sum=find_corrupted_entry(data, 25))
    assert 2980044 == result
    print("Part 2: sum of min-max", result)


if __name__ == "__main__":
    part1()
    part2()
