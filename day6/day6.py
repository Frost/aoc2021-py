from __future__ import annotations
from collections import defaultdict
from icecream import ic


class SchoolOfLanternfish:
    fish: defaultdict[int, int]
    count: int = 0

    def __init__(self) -> None:
        self.fish = defaultdict(int)

    def add_fish(self, clock_day, count=1):
        self.fish[clock_day] += count
        self.count += 1

    def tick(self, days=1) -> int:
        for _day in range(days):
            number_of_new_fish = self.fish[0]

            for i in range(1,9):
                self.fish[i - 1] = self.fish[i]

            self.fish[6] += number_of_new_fish
            self.fish[8] = number_of_new_fish

            self.count += number_of_new_fish

        return self.count


def part1(input) -> int:
    school = SchoolOfLanternfish()

    for fish in input:
        school.add_fish(fish)

    fish_count = school.tick(80)
    return fish_count


def part2(input) -> int:
    school = SchoolOfLanternfish()

    for fish in input:
        school.add_fish(fish)

    fish_count = school.tick(256)
    return fish_count


def read_input() -> list[int]:
    with open("input") as f:
        raw = f.read()

    numbers = list(map(int, raw.strip().split(",")))
    return numbers


if __name__ == "__main__":
    input = read_input()
    school = SchoolOfLanternfish()
    for fish in input:
        school.add_fish(fish)

    part1_answer = school.tick(80)
    part2_answer = school.tick(256 - 80)

    print(part1_answer)
    print(part2_answer)
