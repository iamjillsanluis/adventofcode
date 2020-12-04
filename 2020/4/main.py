def parse_passports():
    passports = []

    current_passport = {}
    with open("input.txt") as fh:
        for line in fh:
            line = line.strip()
            if line == "":
                passports.append(current_passport)
                current_passport = {}
            else:
                for pairs in line.split(" "):
                    key, value = pairs.split(":")
                    current_passport[key] = value

        if current_passport:
            passports.append(current_passport)

    return passports


MANDATORY_PASSPORT_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def is_valid(passport):
    return not MANDATORY_PASSPORT_FIELDS - set(passport.keys())


def part1():
    passports = parse_passports()
    total_valid_passports = len([
        passport
        for passport in passports
        if is_valid(passport)
    ])

    print("Part 1: # valid passports", total_valid_passports)


if __name__ == "__main__":
    part1()
