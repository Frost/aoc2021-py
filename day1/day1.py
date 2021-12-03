from __future__ import annotations


def part1(depths: list[int]):
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1

    return increases


def part2(depths):
    sums = []
    for i in range(3, len(depths)):
        cur = depths[i]
        prev = depths[i - 1]
        pprev = depths[i - 2]

        sums.append(cur + prev + pprev)

    increases = 1
    for i in range(1, len(sums)):
        if sums[i] > sums[i - 1]:
            increases += 1

    return increases


def read_input():
    with open("input") as f:
        return list(map(int, f.readlines()))


if __name__ == "__main__":
    lines = read_input()
    print(part1(lines))
    print(part2(lines))
