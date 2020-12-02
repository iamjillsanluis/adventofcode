def passwords_entries():
    with open("input.txt") as fh:
        for line in fh:
            raw_policy, password = line.strip().split(":")
            yield raw_policy, password.strip()


def total_valid_passwords(entries, policy_cls):
    valid_passwords_count = 0
    for raw_policy, password in entries:
        policy = policy_cls.parse(raw_policy)
        if policy.is_valid(password):
            valid_passwords_count += 1

    return valid_passwords_count


def part1(entries):
    from part1 import Policy
    print("Part 1:", total_valid_passwords(entries, Policy))


def part2(entries):
    from part2 import Policy
    print("Part 2:", total_valid_passwords(entries, Policy))


if __name__ == "__main__":
    passwords_entries = list(passwords_entries())
    part1(passwords_entries)
    part2(passwords_entries)
