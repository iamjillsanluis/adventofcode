def groups_yes_responses(file):
    grouped_responses = [set()]
    with open(file) as fh:
        for line in fh:
            line = line.strip()
            if line == "":
                grouped_responses.append(set())
            else:
                group_index = len(grouped_responses) - 1
                for question in line:
                    grouped_responses[group_index].add(question)
    return grouped_responses


def sum_of_unique_group_responses_count(file):
    grouped_responses = groups_yes_responses(file)
    return sum([
        len(unique_group_responses)
        for unique_group_responses in grouped_responses
    ])


def test():
    assert 11 == sum_of_unique_group_responses_count("test.txt")


if __name__ == "__main__":
    test()