#!/usr/bin/env python3

from pathlib import Path
import os
import sys
from string import Template

day_template = Template(
    """
from icecream import ic


def part1(lines):
    ...


def part2(lines):
    ...


def read_input():
    with open("input") as f:
        f.readlines()


if __name__ == "__main__":
    lines = read_input()
    print(part1(lines))
    print(part2(lines))
"""
)


test_template = Template(
    """
from day$day import *


test_input = []


def test_part1():
    assert part1(test_input) == 0, "Not yet implemented"


def test_part2():
    assert part2(test_input) == 0, "Not yet implemented"
"""
)


if __name__ == "__main__":
    day = sys.argv[1]

    file_path = Path(__file__)
    root_dir = file_path.parent
    dirname = root_dir / f"day{day}"

    os.mkdir(dirname)

    with open(dirname / f"day{day}.py", "w") as f:
        f.write(day_template.substitute())

    with open(dirname / f"test_day{day}.py", "w") as f:
        f.write(test_template.substitute({"day": day}))
