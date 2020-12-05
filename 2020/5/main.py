class BoardingPass:
    def __init__(self, boarding_pass):
        self._boarding_pass = boarding_pass

    def row(self):
        return BoardingPass._decode_pass_data(
            pass_data=self._boarding_pass[:7],
            lower_half_indicator="F"
        )

    def column(self):
        return BoardingPass._decode_pass_data(
            pass_data=self._boarding_pass[-3:],
            lower_half_indicator="L"
        )

    def seat_id(self):
        return self.row() * 8 + self.column()

    @staticmethod
    def _decode_pass_data(pass_data, lower_half_indicator):
        total_characters = len(pass_data)
        min_range = 0
        max_range = (2 ** total_characters) - 1
        current_index = 0

        while current_index < total_characters:
            boundary = int((max_range - min_range) / 2) + min_range
            if pass_data[current_index] == lower_half_indicator:
                max_range = boundary
            else:
                min_range = boundary + 1

            current_index += 1

        return min_range


def test():
    test_cases = {
        "BFFFBBFRRR": (70, 7, 567),
        "FFFBBBFRRR": (14, 7, 119),
        "BBFFBBFRLL": (102, 4, 820)
    }

    for test_case in test_cases:
        boarding_pass = BoardingPass(test_case)
        row, column, seat_id = test_cases[test_case]
        assert boarding_pass.row() == row
        assert boarding_pass.column() == column
        assert boarding_pass.seat_id() == seat_id


def boarding_passes():
    with open("input.txt") as fh:
        for line in fh:
            raw_boarding_pass = line.strip()
            if raw_boarding_pass:
                yield BoardingPass(raw_boarding_pass)


def part1():
    highest_seat_id = 0
    for boarding_pass in boarding_passes():
        highest_seat_id = max(highest_seat_id, boarding_pass.seat_id())

    print("Part 1: highest seat ID", highest_seat_id)


if __name__ == "__main__":
    test()
    part1()