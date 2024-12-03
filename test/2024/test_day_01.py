from pathlib import Path

import pytest

from aoc.utils import Part
from aoc.y2024.d01 import part1, part2


@pytest.mark.parametrize(
    ("part", "input_file", "expected"),
    [
        pytest.param(part1, "data/2024/01-sample", 11, id="part1-sample"),
        pytest.param(part1, "data/2024/01-full", 3246517, id="part1-full"),
        pytest.param(part2, "data/2024/01-sample", 31, id="part2-sample"),
        pytest.param(part2, "data/2024/01-full", 29379307, id="part2-full"),
    ],
)
def test_day_01(part: Part, input_file: str, expected: int):
    if not (input_path := Path(input_file)).exists():
        pytest.skip(reason=f"data file not found: '{input_path}'")

    actual = part(input_path.read_text("utf-8"))
    assert actual == expected
