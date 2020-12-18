def solve_1(lines):
    return next((a * b) for a in lines for b in lines if a + b == 2020)


def solve_2(lines):
    return next(
        (a * b * c) for a in lines for b in lines for c in lines if a + b + c == 2020
    )


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [int(line) for line in input_file.read().splitlines()]

    print(solve_1(lines))
    print(solve_2(lines))
