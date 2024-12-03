import re

from aoc.utils import runner


def process_muls_in_text(text: str) -> int:
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    result = 0
    for a, b in pattern.findall(text):
        result += int(a) * int(b)
    return result


def part1(input_data: str):
    result = process_muls_in_text(input_data)

    return result


def part2(input_data: str):
    dos = input_data.split("do()")

    result = 0
    for do in dos:
        do = do.split("don't()")[0]
        result += process_muls_in_text(do)

    return result


if __name__ == "__main__":
    runner([(part1, 161), (part2, 48)])
