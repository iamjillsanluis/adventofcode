import re


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
        if all([validator(passport) for validator in validators])
    ])


def part1():
    print("Part 1: # valid passports", total_valid_passports([has_all_mandatory_fields]))


def parse_year(passport, year_field):
    try:
        return int(passport.get(year_field, 0))
    except ValueError:
        return 0


def has_valid_height(raw_height):
    matches = re.search("^(\\d+)(in|cm)$", raw_height)
    if not matches:
        return False

    height = int(matches[1])
    height_unit = matches[2]

    return {
        "cm": lambda h: 150 <= h <= 193,
        "in": lambda h: 59 <= h <= 76
    }[height_unit](height)


def part2():
    validators = [
        has_all_mandatory_fields,
        lambda passport: 1920 <= parse_year(passport, "byr") <= 2002,
        lambda passport: 2010 <= parse_year(passport, "iyr") <= 2020,
        lambda passport: 2020 <= parse_year(passport, "eyr") <= 2030,
        lambda passport: has_valid_height(passport.get("hgt", "")),
        lambda passport: bool(re.search("^#([a-f]|\\d){6}$", passport.get("hcl", ""))),
        lambda passport: bool(re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", passport.get("ecl", ""))),
        lambda passport: bool(re.search("^\\d{9}$", passport.get("pid", ""))),
    ]
    print("Part 2: # valid passports", total_valid_passports(validators))


if __name__ == "__main__":
    part1()
    part2()
