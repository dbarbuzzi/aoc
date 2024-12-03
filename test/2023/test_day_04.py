from pathlib import Path

import pytest

from aoc.utils import Part
from aoc.y2023.d04 import part1, part2


@pytest.mark.parametrize(
    ("part", "input_file", "expected"),
    [
        pytest.param(part1, "data/2023/04-sample", 13, id="part1-sample"),
        pytest.param(part1, "data/2023/04-full", 25571, id="part1-full"),
        pytest.param(part2, "data/2023/04-sample", 30, id="part2-sample"),
        pytest.param(part2, "data/2023/04-full", 8805731, id="part2-full"),
    ],
)
def test_day_04(part: Part, input_file: str, expected: int):
    if not (input_path := Path(input_file)).exists():
        pytest.skip(reason=f"data file not found: '{input_path}'")

    actual = part(input_path.read_text("utf-8"))
    assert actual == expected
