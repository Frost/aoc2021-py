
from day13 import *


test_input = []

test_input = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".strip()


def test_fold_x():
    ...


def test_fold_y():
    ...


def test_part1():
    dots, folds = parse_input(test_input)
    assert part1(dots, folds) == 17
