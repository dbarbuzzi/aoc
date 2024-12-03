from aoc.utils import runner


def is_safe(report: list[int], max_threshold: int = 3) -> bool:
    if report not in (sorted(report), sorted(report, reverse=True)):
        return False

    report = sorted(report)
    for a, b in zip(report[:-1], report[1:]):
        if a == b or abs(a - b) > max_threshold:
            return False

    return True


def is_damp_safe(report: list[int], max_threshold: int = 3) -> bool:
    dampened_reports: list[list[int]] = []
    for i in range(len(report)):
        dampened_reports.append([*report[:i], *report[i + 1 :]])

    for dampened_report in dampened_reports:
        if is_safe(dampened_report, max_threshold=max_threshold):
            return True

    return False


def part1(input_data: str):
    reports: list[list[int]] = [
        [*map(int, line.split())] for line in input_data.splitlines()
    ]

    result = sum(is_safe(report) for report in reports)

    return result


def part2(input_data: str):
    reports: list[list[int]] = [
        [*map(int, line.split())] for line in input_data.splitlines()
    ]

    result = sum(is_damp_safe(report) for report in reports)

    return result


if __name__ == "__main__":
    runner([(part1, 2), (part2, 4)])
