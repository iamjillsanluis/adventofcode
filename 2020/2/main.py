def passwords_entries():
    with open("input.txt") as fh:
        for line in fh:
            raw_policy, password = line.strip().split(":")
            yield raw_policy, password.strip()


def part1(entries):
    from part1 import total_valid_passwords
    print("Part 1:", total_valid_passwords(entries))


def part2(entries):
    from part2 import total_valid_passwords
    print("Part 2:", total_valid_passwords(entries))


if __name__ == "__main__":
    passwords_entries = passwords_entries()
    part1(passwords_entries)
    part2(passwords_entries)
