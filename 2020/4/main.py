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


def has_all_mandatory_fields(passport):
    return not MANDATORY_PASSPORT_FIELDS - set(passport.keys())


def total_valid_passports(validators):
    passports = parse_passports()
    return len([
        passport
        for passport in passports
        if all(validator(passport) for validator in validators)
    ])


def part1():
    print("Part 1: # valid passports", total_valid_passports([has_all_mandatory_fields]))


if __name__ == "__main__":
    part1()
