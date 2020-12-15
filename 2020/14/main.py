import re


def parse_program(file):
    groups = []

    current_bit_mask = {}
    current_instructions = []
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            matches = re.search(r"^mask = ([X|1|0]{36})$", line)
            if matches:
                if current_bit_mask:
                    groups.append((current_bit_mask, current_instructions))
                    current_bit_mask = {}
                    current_instructions = []

                for index, bit in enumerate(matches[1]):
                    if bit != "X":
                        current_bit_mask[35-index] = int(bit)
            else:
                matches = re.search(r"^mem\[(\d+)\] = (\d+)$", line)
                if matches:
                    current_instructions.append((int(matches[1]), int(matches[2])))

    if current_bit_mask:
        groups.append((current_bit_mask, current_instructions))

    return groups


def mask(bit_mask, value):
    def to_binary_list(decimal):
        binary = [0] * 36

        for bit_index in reversed(range(36)):
            binary_digit = 2 ** bit_index
            binary[bit_index] = int(decimal / binary_digit)
            decimal = decimal % binary_digit

        return binary

    def to_decimal(binary_list):
        decimal = 0
        for exp, bit in enumerate(binary_list):
            decimal += (2 ** exp) * bit
        return decimal

    binary_value = to_binary_list(value)
    for bit_index in bit_mask:
        binary_value[bit_index] = bit_mask[bit_index]

    return to_decimal(binary_value)


def sum_memory_values(file):
    memory = {}
    for bit_mask, instructions in parse_program(file):
        for address, value in instructions:
            memory[address] = mask(bit_mask, value)

    return sum(
        x for x in memory.values()
    )


def test1():
    assert 165 == sum_memory_values("short_input.txt")


def part1():
    # test1()
    print("Part 1: sum", sum_memory_values("input.txt"))


if __name__ == "__main__":
    part1()
