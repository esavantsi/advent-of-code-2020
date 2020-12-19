import re

passport_field_re = re.compile(r"(\w+):([^\s]+)")


def _get_passport_datas(lines):
    raw_passport = ""
    for line in lines:
        if line == "":
            yield raw_passport
            raw_passport = ""
        else:
            raw_passport += f"{line} "
    yield raw_passport


def _get_passports(lines):
    passport_datas = (
        re.findall(passport_field_re, passport)
        for passport in _get_passport_datas(lines)
    )
    return (dict(passport_data) for passport_data in passport_datas)


def solve_1(lines):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    passports = _get_passports(lines)

    valid_passports = [
        passport
        for passport in passports
        if all(field in passport for field in required_fields)
    ]

    return len(valid_passports)


def solve_2(lines):
    hgt_re = re.compile(r"^(\d+)(in|cm)$")
    hcl_re = re.compile(r"^#[a-f0-9]{6}$")
    pid_re = re.compile(r"^[\d]{9}$")

    def _validate_hgt(value):
        if not (match := hgt_re.match(value)):
            return False

        height, unit = match.groups()

        if unit == "cm":
            return 150 <= int(height) <= 193
        else:
            return 59 <= int(height) <= 76

    required_fields = (
        ("byr", lambda v: 1920 <= int(v) <= 2002),
        ("iyr", lambda v: 2010 <= int(v) <= 2020),
        ("eyr", lambda v: 2020 <= int(v) <= 2030),
        ("hgt", _validate_hgt),
        ("hcl", lambda v: bool(hcl_re.match(v))),
        ("ecl", lambda v: v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
        ("pid", lambda v: bool(pid_re.match(v))),
    )

    passports = _get_passports(lines)

    valid_passports = [
        passport
        for passport in passports
        if all(
            field in passport and validator(passport[field])
            for field, validator in required_fields
        )
    ]

    return len(valid_passports)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = input_file.read().splitlines()

    print(solve_1(lines))
    print(solve_2(lines))
