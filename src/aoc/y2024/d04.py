from aoc.utils import runner


def part1(input_data: str) -> int:
    grid = input_data.splitlines()
    count = 0

    num_rows = len(grid)
    num_cols = len(grid[0])

    for y, row in enumerate(grid):
        # first, get any horizontal/single-row matches; no need to anchor on "X"
        count += row.count("XMAS") + row.count("SAMX")

        for x, cell in enumerate(row):
            # for remaining checks, use first letter ("X") as anchor point
            if cell != "X":
                continue

            # if y >= 3: check upward
            if y >= 3:
                # straight up
                if (
                    grid[y - 1][x] == "M"
                    and grid[y - 2][x] == "A"
                    and grid[y - 3][x] == "S"
                ):
                    count += 1
                # up-left
                if (
                    x >= 3
                    and grid[y - 1][x - 1] == "M"
                    and grid[y - 2][x - 2] == "A"
                    and grid[y - 3][x - 3] == "S"
                ):
                    count += 1
                # up-right
                if (
                    x < num_cols - 3
                    and grid[y - 1][x + 1] == "M"
                    and grid[y - 2][x + 2] == "A"
                    and grid[y - 3][x + 3] == "S"
                ):
                    count += 1
            # if y < num_rows - 3: check downward
            if y < num_rows - 3:
                # straight down
                if (
                    grid[y + 1][x] == "M"
                    and grid[y + 2][x] == "A"
                    and grid[y + 3][x] == "S"
                ):
                    count += 1
                # down-left
                if (
                    x >= 3
                    and grid[y + 1][x - 1] == "M"
                    and grid[y + 2][x - 2] == "A"
                    and grid[y + 3][x - 3] == "S"
                ):
                    count += 1
                # down-right
                if (
                    x < num_cols - 3
                    and grid[y + 1][x + 1] == "M"
                    and grid[y + 2][x + 2] == "A"
                    and grid[y + 3][x + 3] == "S"
                ):
                    count += 1

    return count


def part2(input_data: str) -> int:
    grid = input_data.splitlines()
    count = 0

    for y, row in enumerate(grid[1:-1], start=1):
        for x, cell in enumerate(row[1:-1], start=1):
            # find anchor-point "A"s to work off of
            if cell != "A":
                continue

            if (
                (  # "M"s on top
                    grid[y - 1][x - 1] == grid[y - 1][x + 1] == "M"
                    and grid[y + 1][x - 1] == grid[y + 1][x + 1] == "S"
                )
                or (  # "M"s on bottom
                    grid[y + 1][x - 1] == grid[y + 1][x + 1] == "M"
                    and grid[y - 1][x - 1] == grid[y - 1][x + 1] == "S"
                )
                or (  # "M"s on left
                    grid[y - 1][x - 1] == grid[y + 1][x - 1] == "M"
                    and grid[y - 1][x + 1] == grid[y + 1][x + 1] == "S"
                )
                or (  # "M"s on right
                    grid[y - 1][x + 1] == grid[y + 1][x + 1] == "M"
                    and grid[y + 1][x - 1] == grid[y - 1][x - 1] == "S"
                )
            ):
                count += 1

    return count


if __name__ == "__main__":
    runner([(part1, 18), (part2, 9)])
