
from collections import defaultdict
from icecream import ic


def part1(lines):
    number_of_unique_output_values = 0
    for line in lines:
        _in, out = line.split(" | ")
        for v in out.split(" "):
            if len(v) in [2,3,4,7]:
                number_of_unique_output_values += 1

    return number_of_unique_output_values


def part2(lines):
    return sum(map(calculate_output_value, lines))


def calculate_output_value(line):
    ins, out = line.split(" | ")
    input_values = defaultdict(list)
    translate = dict()
    zero_six_nine = list()
    two_three_five = list()
    one = None
    four = None
    seven = None
    eight = None
    for i in ins.strip().split(" "):
        iset = frozenset(i)
        input_values[len(i)].append(iset)
        match len(iset):
            case 2:
                one = iset
                translate[one] = 1
            case 3:
                seven = iset
                translate[seven] = 7
            case 4:
                four = iset
                translate[four] = 4
            case 7:
                eight = iset
                translate[eight] = 8
            case 5:
                two_three_five.append(iset)
            case 6:
                zero_six_nine.append(iset)

    for n in zero_six_nine:
        ns = frozenset(n)
        if ns | one == eight:
            translate[ns] = 6
        elif ns | four == eight:
            translate[ns] = 0
        else:
            translate[ns] = 9

    for n in two_three_five:
        ns = frozenset(n)
        if len(ns - four) == 3:
            translate[ns] = 2
        elif ns | one == ns:
            translate[ns] = 3
        else:
            translate[ns] = 5

    output = "".join([str(translate[frozenset(o)]) for o in out.strip().split(" ")])

    return int(output)


def read_input():
    with open("input") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    lines = read_input()
    print(part1(lines))
    print(part2(lines))
