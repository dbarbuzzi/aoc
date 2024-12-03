from aoc.utils import runner


def _prep_line(line: str) -> str:
    number_map = {
        "": "",
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    for k, v in number_map.items():
        line = line.replace(k, v)
    return line


def part1(input_data: str) -> int:
    line_numbers: list[int] = []
    for line in input_data.splitlines():
        digits = [int(c) for c in line if c.isdigit()]
        line_numbers.append(digits[0] * 10 + digits[-1])
    return sum(line_numbers)


def part2(input_data: str) -> int:
    line_numbers: list[int] = []
    for line in input_data.splitlines():
        line = _prep_line(line)
        digits = [int(c) for c in line if c.isdigit()]
        line_numbers.append(digits[0] * 10 + digits[-1])
    return sum(line_numbers)


if __name__ == "__main__":
    runner([(part1, 142), (part2, 281, "01-sample-2")])
