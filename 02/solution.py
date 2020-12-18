import re

prog = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


def solve_1(lines):
    count = 0

    for line in lines:
        match = prog.match(line)
        min_amount, max_amount, char, password = match.groups()

        if int(min_amount) <= password.count(char) <= int(max_amount):
            count += 1

    return count


def solve_2(lines):
    count = 0

    for line in lines:
        match = prog.match(line)
        position_1, position_2, char, password = match.groups()

        position_1_has_char = password[int(position_1) - 1] == char
        position_2_has_char = password[int(position_2) - 1] == char

        if position_1_has_char ^ position_2_has_char:
            count += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = input_file.read().splitlines()

    print(solve_1(lines))
    print(solve_2(lines))
