import argparse
from dataclasses import dataclass
from datetime import date
from pathlib import Path

TODAY = date.today()
CURRENT_DAY = f"{TODAY.day}"
CURRENT_YEAR = f"{TODAY.year}"
CWD = Path(__file__)


def day(text: str) -> int:
    day_num = int(text)
    assert 1 <= day_num <= 25
    return day_num


@dataclass
class Config:
    day: str
    year: str

    @staticmethod
    def from_namespace(args: argparse.Namespace) -> "Config":
        return Config(f"{args.day:02}", str(args.year))


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=day, default=CURRENT_DAY)
    parser.add_argument("-y", "--year", type=int, default=CURRENT_YEAR)
    return Config.from_namespace(parser.parse_args())


if __name__ == "__main__":
    config = parse_args()

    files = {
        "data-full": Path("./data") / config.year / f"{config.day}-full",
        "data-sample": Path("./data") / config.year / f"{config.day}-sample",
        "source": Path("./src/aoc") / f"y{config.year}" / f"d{config.day}.py",
        "test": Path("./test") / config.year / f"test_day_{config.day}.py",
    }
    templates = {
        "source": CWD.with_name("template-source.txt"),
        "test": CWD.with_name("template-test.txt"),
    }

    # use touch to safely create empty data files if they don't exist
    for file_key in ["data-full", "data-sample"]:
        print(f"touching {files[file_key]}")
        files[file_key].touch()

    # create source file from template if it doesn't exist
    if not files["source"].exists():
        print(f"writing '{files['source']}'")
        template = Path(templates["source"]).read_text(encoding="utf-8")
        files["source"].write_text(template)
    else:
        print(f"source file already exists: '{files['source']}'")

    # create test file from template if it doesn't exist
    if not files["test"].exists():
        print(f"writing '{files['test']}'")
        template = Path(templates["test"]).read_text(encoding="utf-8")
        files["test"].write_text(template.format(year=config.year, day=config.day))
    else:
        print(f"test file already exists: '{files['test']}'")
