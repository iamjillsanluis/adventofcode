from dataclasses import dataclass


@dataclass
class Policy:
    target: str
    min_occurrence: int
    max_occurrence: int

    @staticmethod
    def parse(raw_policy):
        range_spec, character = raw_policy.split(" ")
        min_occurrence, max_occurrence = range_spec.split("-")
        return Policy(target=character, min_occurrence=int(min_occurrence), max_occurrence=int(max_occurrence))

    def is_valid(self, password):
        total_occurrence = 0
        for char in password:
            if self.target == char:
                total_occurrence += 1

        return self.min_occurrence <= total_occurrence <= self.max_occurrence
