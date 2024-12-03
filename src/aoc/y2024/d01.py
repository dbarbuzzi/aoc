from collections import Counter

from aoc.utils import runner


def separate_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    for line in lines:
        left_n, right_n = map(int, line.split())
        left.append(left_n)
        right.append(right_n)

    return left, right


def part1(input_data: str):
    lines = input_data.splitlines()
    left, right = separate_lists(lines)

    left.sort()
    right.sort()

    result = 0
    for m, n in zip(left, right):
        result += abs(m - n)

    return result


def part2(input_data: str):
    lines = input_data.splitlines()
    left, right = separate_lists(lines)
    counter = Counter(right)

    result = 0
    for num in left:
        result += num * counter.get(num, 0)

    return result


if __name__ == "__main__":
    runner([(part1, 11), (part2, 31)])
