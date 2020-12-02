from dataclasses import dataclass


@dataclass
class Policy:
    target: str
    first_position: int
    second_position: int


def is_valid_password(policy, password):
    first_char = password[policy.first_position]
    second_char = password[policy.second_position]
    return (first_char == policy.target or second_char == policy.target) and first_char != second_char


def as_policy(raw_policy):
    range_spec, character = raw_policy.split(" ")
    first_position, second_position = range_spec.split("-")
    return Policy(target=character, first_position=int(first_position)-1, second_position=int(second_position)-1)


def total_valid_passwords(entries):
    valid_passwords_count = 0
    for raw_policy, password in entries:
        policy = as_policy(raw_policy)
        if is_valid_password(policy, password):
            valid_passwords_count += 1

    return valid_passwords_count

