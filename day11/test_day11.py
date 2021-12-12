
from day11 import *


test_input = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""



def test_cave_constructor():
    cave = Cave(["12", "34"])
    assert cave.energy_levels() == [[1,2], [3,4]]


def test_simple_tick():
    test_data = """
    11111
    19991
    19191
    19991
    11111
    """.strip().split("\n")

    cave = Cave(test_data)
    assert cave.tick() == 9

    assert cave.energy_levels() == [
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3],
    ]

    assert cave.tick() == 0

    assert cave.energy_levels() == [
        [4,5,6,5,4],
        [5,1,1,1,5],
        [6,1,1,1,6],
        [5,1,1,1,5],
        [4,5,6,5,4],
    ]


def test_flashes():
    lines = test_input.strip().split("\n")
    cave = Cave(lines)

    assert cave.tick() == 0
    assert cave.tick() == 35


def test_part1():
    lines = test_input.strip().split("\n")
    assert part1(lines) == 1656


def test_part2():
    lines = test_input.strip().split("\n")
    assert part2(lines) == 195
