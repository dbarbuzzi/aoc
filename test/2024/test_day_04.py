from pathlib import Path

import pytest

from aoc.utils import Part
from aoc.y2024.d04 import part1, part2


@pytest.mark.parametrize(
    ("part", "input_file", "expected"),
    [
        pytest.param(part1, "data/2024/04-sample", 18, id="part1-sample"),
        pytest.param(part1, "data/2024/04-full", 2593, id="part1-full"),
        pytest.param(part2, "data/2024/04-sample", 9, id="part2-sample"),
        pytest.param(part2, "data/2024/04-full", 1950, id="part2-full"),
    ],
)
def test_day_04(part: Part, input_file: str, expected: int):
    if not (input_path := Path(input_file)).exists():
        pytest.skip(reason=f"data file not found: '{input_path}'")

    actual = part(input_path.read_text("utf-8"))
    assert actual == expected
