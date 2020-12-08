from dataclasses import dataclass


@dataclass
class Instruction:
    index: int
    name: str
    value: int


def parse_advent_assembly(file):
    instructions = []
    with open(file) as fh:
        index = 0
        for line in fh:
            name, value = line.strip().split(" ")
            instructions.append(Instruction(index, name, int(value)))
            index += 1
    return instructions


def ordered_instructions(instructions):
    loop_detectable_instructions = []
    current_instruction_index = 0
    for _ in range(0, len(instructions) * 2):
        current_instruction = instructions[current_instruction_index]
        loop_detectable_instructions.append(current_instruction)

        if current_instruction.name == "jmp":
            current_instruction_index += current_instruction.value
        else:
            current_instruction_index += 1
    return loop_detectable_instructions


def resolve_looper_index(instructions):
    visited_instruction = set()
    for index, instruction in enumerate(instructions):
        if instruction.index in visited_instruction:
            return index
        else:
            visited_instruction.add(instruction.index)
    return -1


def accumulator_value(instructions):
    return sum([
        instruction.value
        for instruction in instructions
        if instruction.name == "acc"
    ])


def accumulator_value_after_loop(file):
    instructions = ordered_instructions(parse_advent_assembly(file))
    looper_index = resolve_looper_index(instructions)

    return accumulator_value(instructions[0:looper_index])


def test1():
    assert 5 == accumulator_value_after_loop("short_input.txt")


def part1():
    print("Part 1: accumulator", accumulator_value_after_loop("input.txt"))


if __name__ == "__main__":
    test1()
    part1()
