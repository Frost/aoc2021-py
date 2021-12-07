
from day7 import *


test_input = [16,1,2,0,4,2,7,1,2,14]


def test_triangular_distance():
    assert triangular_distance(1, 5) == 10


def test_part1():
    assert part1(test_input) == 37


def test_part2():
    assert part2(test_input) == 168, "Not yet implemented"
