from dataclasses import dataclass


@dataclass
class Policy:
    target: str
    min_occurrence: int
    max_occurrence: int


def is_valid_password(policy, password):
    total_occurrence = 0
    for char in password:
        if policy.target == char:
            total_occurrence += 1

    return policy.min_occurrence <= total_occurrence <= policy.max_occurrence


def as_policy(raw_policy):
    range_spec, character = raw_policy.split(" ")
    min_occurrence, max_occurrence = range_spec.split("-")
    return Policy(target=character, min_occurrence=int(min_occurrence), max_occurrence=int(max_occurrence))


def total_valid_passwords(entries):
    valid_passwords_count = 0
    for raw_policy, password in entries:
        policy = as_policy(raw_policy)
        if is_valid_password(policy, password):
            valid_passwords_count += 1

    return valid_passwords_count

