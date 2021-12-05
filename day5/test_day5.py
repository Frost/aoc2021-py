
from day5 import *


test_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

def test_vertical_line():
    line = Line("1,1", "1,3")
    assert line.is_vertical()
    assert line.coordinates() == [
        Coordinate(1,1),
        Coordinate(1,2),
        Coordinate(1,3),
    ]

def test_horizontal_line():
    line = Line("9,7", "7,7")
    assert line.is_horizontal()
    assert line.coordinates() == [
        Coordinate(7,7),
        Coordinate(8,7),
        Coordinate(9,7),
    ]

def test_diagonal_line():
    line = Line("1,1", "3,3")
    assert line.is_diagonal()
    assert line.coordinates() == [
        Coordinate(1,1),
        Coordinate(2,2),
        Coordinate(3,3),
    ]


def test_part1():
    lines = format_input(test_input)
    assert part1(lines) == 5


def test_part2():
    lines = format_input(test_input)
    assert part2(lines) == 12
