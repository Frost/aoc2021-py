from icecream import ic


def triangular_distance(src, dest):
    diff = abs(src - dest)
    return int(diff * ( diff + 1 ) / 2)


def calc_sum(numbers, cmp):
    distances = [triangular_distance(i, cmp) for i in numbers]
    return sum(distances)


def part1(numbers):
    sorted_input = sorted(numbers)
    count = len(sorted_input)
    median = sorted_input[int(count / 2)]
    diffs = [abs(i - median) for i in sorted_input]
    return sum(diffs)


def part2(numbers):
    sorted_input = sorted(numbers)
    lowest = min(sorted_input)
    highest = max(sorted_input)

    smallest = None

    for number in range(lowest, highest + 1):
        count = calc_sum(sorted_input, number)
        if smallest is None or count < smallest:
            smallest = count

    return smallest


def read_input():
    with open("input") as f:
        return list(map(int, f.readline().strip().split(",")))


if __name__ == "__main__":
    lines = read_input()
    print(part1(lines))
    lines = read_input()
    print(part2(lines))
