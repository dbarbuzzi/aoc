import inspect
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

from rich.console import Console

console = Console(highlight=False)

Part = Callable[[str], int]


@dataclass
class Solution:
    func: Part
    sample_answer: int
    sample_data_key: Optional[str] = None


def get_input_data(year: str, day: str) -> dict[str, str]:
    path = Path("data") / year
    files: dict[str, str] = {}
    for file in path.glob(f"{day}-*"):
        files[file.name] = file.read_text(encoding="utf-8")

    return files


def get_importer() -> str:
    # get name of importing file
    # source: https://stackoverflow.com/a/52313172
    # adjusted to `inspect.stack()[2:]` due to extra frame from being within function
    if __name__ != "__main__":
        for frame in inspect.stack()[2:]:
            if frame.filename[0] != "<":
                return frame.filename

    raise RuntimeError("didn't expect to get here")


def runner(parts: list[tuple[Part, int] | tuple[Part, int, str]]):
    path = Path(get_importer()).resolve().as_posix()

    year_re = re.compile(r"\d{4}")
    year = year_re.search(path)
    assert year is not None
    year = year.group(0)

    day_re = re.compile(r"\d{2}")
    day = day_re.search(path.split("/")[-1])
    assert day is not None
    day = day.group(0)

    input_data = get_input_data(year, day)

    for i, part in enumerate(parts, start=1):
        solution = Solution(*part)  # type: ignore

        # print sample execution/expectation
        sample_data_key = solution.sample_data_key or f"{day}-sample"
        if not (sample_data := input_data.get(sample_data_key)):
            raise RuntimeError("no sample data found for key '{sample_data_key}'")

        try:
            answer = solution.func(sample_data)

            answer_color = "green" if answer == part[1] else "red"
            expected_color = "green" if answer == part[1] else "cyan"

            console.rule(f"{year} / {day} / PART {i}", style=answer_color)
            console.print(
                f"sample: [{answer_color}]{answer}[/{answer_color}] "
                f"(expected: [{expected_color}]{part[1]}[/{expected_color}])"
            )

            # print full execution
            print(f"  full: {solution.func(input_data[f"{day}-full"])}")
        except NotImplementedError:
            console.rule(f"{year} / {day} / PART {i}", style="yellow")
            print("TODO")
