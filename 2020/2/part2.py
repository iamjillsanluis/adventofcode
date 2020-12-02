from dataclasses import dataclass


@dataclass
class Policy:
    target: str
    first_position: int
    second_position: int

    @staticmethod
    def parse(raw_policy):
        range_spec, character = raw_policy.split(" ")
        first_position, second_position = range_spec.split("-")
        return Policy(target=character, first_position=int(first_position) - 1,
                      second_position=int(second_position) - 1)

    def is_valid(self, password):
        first_char = password[self.first_position]
        second_char = password[self.second_position]
        return (first_char == self.target or second_char == self.target) and first_char != second_char
