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
    total_instructions = len(instructions)
    loop_detectable_instructions = []
    current_instruction_index = 0
    for _ in range(0, total_instructions * 2):
        if current_instruction_index >= total_instructions:
            break

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


def altered_instructions(template_instructions, instruction_to_alter):
    alternative_name = {
        "jmp": "nop",
        "nop": "jmp"
    }[instruction_to_alter.name]

    instructions = template_instructions.copy()
    instructions[instruction_to_alter.index] = Instruction(
        index=instruction_to_alter.index,
        name=alternative_name,
        value=instruction_to_alter.value
    )

    return instructions


def non_looping_altered_instructions(file):
    initial_instructions = parse_advent_assembly(file)
    for initial_instruction in initial_instructions:
        if initial_instruction.name != "acc":
            looping_candidate = altered_instructions(
                template_instructions=initial_instructions,
                instruction_to_alter=initial_instruction
            )
            if resolve_looper_index(ordered_instructions(looping_candidate)) < 0:
                return looping_candidate

    return []


def accumulator_value_after_terminating_instructions(file):
    non_looping_instructions = non_looping_altered_instructions(file)
    reduced_instructions = []
    current_instruction_index = 0
    for _ in range(0, len(non_looping_instructions)):
        if current_instruction_index >= len(non_looping_instructions):
            break

        current_instruction = non_looping_instructions[current_instruction_index]
        reduced_instructions.append(current_instruction)
        if current_instruction.name == "jmp":
            current_instruction_index += current_instruction.value
        else:
            current_instruction_index += 1

    return accumulator_value(reduced_instructions)


def test2():
    assert 8 == accumulator_value_after_terminating_instructions("short_input.txt")


def part2():
    print("Part 2: accumulator", accumulator_value_after_terminating_instructions("input.txt"))


if __name__ == "__main__":
    test1()
    part1()

    test2()
    part2()
