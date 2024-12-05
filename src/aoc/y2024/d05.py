from collections import defaultdict

from aoc.utils import runner


def build_ruleset(rules: str) -> dict[str, set[str]]:
    ruleset: dict[str, set[str]] = defaultdict(set)
    for line in rules.splitlines():
        a, b = line.split("|")
        ruleset[a].add(b)
    return ruleset


def in_order(pages: list[str], ruleset: dict[str, set[str]]) -> bool:
    for i, page in enumerate(pages):
        if i == 0:
            continue

        for prev_page in pages[:i]:
            if prev_page in ruleset[page]:
                return False
    return True


def part1(input_data: str) -> int:
    rules, updates = input_data.split("\n\n")
    ruleset = build_ruleset(rules)

    result = 0
    for update in updates.splitlines():
        pages = update.split(",")
        if in_order(pages, ruleset):
            result += int(pages[len(pages) // 2])
    return result


def sort_pages(pages: list[str], ruleset: dict[str, set[str]]) -> list[str]:
    for i in range(1, len(pages)):
        page = pages[i]
        for j, prev_page in enumerate(pages[:i]):
            if prev_page in ruleset[page]:
                pages = pages[:i] + pages[i + 1 :]  # remove from current position
                pages.insert(j, page)  # insert before prev_page
                break  # no need to keep moving the number
    return pages


def part2(input_data: str) -> int:  # 4344 -- too low :\
    rules, updates = input_data.split("\n\n")
    ruleset = build_ruleset(rules)

    result = 0
    for update in updates.splitlines():
        pages = update.split(",")
        if in_order(pages, ruleset):
            continue
        pages = sort_pages(pages, ruleset)
        assert in_order(pages, ruleset), "page order is incorrect"
        result += int(pages[len(pages) // 2])
    return result


if __name__ == "__main__":
    runner([(part1, 143), (part2, 123)])
