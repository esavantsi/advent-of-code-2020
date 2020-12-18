import math

OPEN_SQUARE = "."
TREE = "#"


def _make_path(dx, dy, y_len):
    return ((n * dx, n * dy) for n in range(0, math.ceil(y_len / dy)))


def _tree_encounters(lines, path):
    line_lenth = len(lines[0])  # Lines are of equal length
    encounters = (lines[y][x % line_lenth] for (x, y) in path)
    trees = [encounter for encounter in encounters if encounter == TREE]
    return len(trees)


def solve_1(lines):
    path = _make_path(3, 1, len(lines))
    return _tree_encounters(lines, path)


def solve_2(lines):
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )

    paths = (_make_path(dx, dy, len(lines)) for dx, dy in slopes)
    tree_encounters = (_tree_encounters(lines, path) for path in paths)
    return math.prod(tree_encounters)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = input_file.read().splitlines()

    print(solve_1(lines))
    print(solve_2(lines))
