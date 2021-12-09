
from day9 import *


test_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_part1():
    matrix = create_matrix(test_input)
    assert part1(matrix) == 15


def test_part2():
    matrix = create_matrix(test_input)
    assert part2(matrix) == 1134
