import pytest
from day3 import *

test_lines = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_calculate_power():
    power = calculate_power(test_lines)

    assert power.gamma == 22
    assert power.epsilon == 9


def test_filter_oxygen():
    assert filter_rating(test_lines, "gamma") == 23


def test_filter_co2():
    assert filter_rating(test_lines, "epsilon") == 10


def test_part1():
    assert part1(test_lines) == 198


def test_part2():
    assert part2(test_lines) == 230
