def data_feed(file):
    data = []
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line:
                data.append(int(line))

    return data


def has_summing_pairs(pre_amble, target_sum):
    for augend_index, augend in enumerate(pre_amble[:-1]):
        for addend in pre_amble[augend_index + 1:]:
            sum_candidate = augend + addend
            if sum_candidate == target_sum:
                return True
    return False


def find_corrupted_entry(data, pre_amble_size):
    candidates = []
    for sum_candidate_index in range(pre_amble_size, len(data)):
        pre_amble = data[sum_candidate_index - pre_amble_size:sum_candidate_index]
        target_sum = data[sum_candidate_index]
        if not has_summing_pairs(pre_amble, target_sum):
            candidates.append(target_sum)

    if len(candidates) == 1:
        return candidates[0]
    return None


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
    print("Part 1: corrupted entry:", find_corrupted_entry(data_feed("input.txt"), 25))


def test2():
    assert 62 == find_contiguous_range_min_max_sum(data_feed("short_input.txt"), 127)


def part2():
    test2()
    data = data_feed("input.txt")
    print(
        "Part 2: sum of min-max",
        find_contiguous_range_min_max_sum(
            data,
            target_sum=find_corrupted_entry(data, 25)
        )
    )


if __name__ == "__main__":
    part1()
    part2()
