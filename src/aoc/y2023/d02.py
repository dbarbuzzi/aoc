import re

from aoc.utils import runner


def parse_line(line: str) -> tuple[int, list[dict[str, int]]]:
    game_id, draws_text = line.split(": ")
    game_id = int(game_id.split()[1])
    draws: list[dict[str, int]] = []
    for draw_text in draws_text.split("; "):
        draw = {"red": 0, "green": 0, "blue": 0}
        for color in draw.keys():
            if matches := re.search(rf"\b(\d+) {color}", draw_text):
                draw[color] = int(matches[1])
        draws.append(draw)
    return game_id, draws


def max_draws(draws: list[dict[str, int]]) -> dict[str, int]:
    maxes = {"red": 0, "green": 0, "blue": 0}
    for draw in draws:
        for color in draw.keys():
            maxes[color] = max(draw[color], maxes[color])
    return maxes


def game_is_possible(draws: list[dict[str, int]], config: dict[str, int]) -> bool:
    maxes = max_draws(draws)
    return (
        maxes["red"] <= config["red"]
        and maxes["green"] <= config["green"]
        and maxes["blue"] <= config["blue"]
    )


def part1(input_data: str):
    base_config = {"red": 12, "green": 13, "blue": 14}
    id_sum = 0
    for line in input_data.splitlines():
        game_id, draws = parse_line(line)
        if game_is_possible(draws, base_config):
            id_sum += game_id

    return id_sum


def part2(input_data: str):
    total_power = 0
    for line in input_data.splitlines():
        _, draws = parse_line(line)
        maxes = max_draws(draws)
        draw_power = maxes["red"] * maxes["green"] * maxes["blue"]
        total_power += draw_power

    return total_power


if __name__ == "__main__":
    runner([(part1, 8), (part2, 2286)])
