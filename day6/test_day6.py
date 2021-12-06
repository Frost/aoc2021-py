
from day6 import *


test_input = [3,4,3,1,2]


def test_school():
    school = SchoolOfLanternfish()
    for fish in test_input:
        school.add_fish(fish)

    assert school.count == 5

    count_after_18_days = school.tick(18)

    assert count_after_18_days == 26



def test_part1():
    assert part1(test_input) == 5934


def test_part2():
    assert part2(test_input) == 26984457539, "Not yet implemented"
