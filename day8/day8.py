
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
    translation_map = dict()
    zero_six_nine = list()
    two_three_five = list()
    one = None
    four = None
    seven = None
    eight = None
    for i in ins.strip().split(" "):
        input_values[len(i)].append("".join(sorted(i)))
        s = "".join(sorted(i))
        match len(s):
            case 2:
                one = set(s)
                translation_map[s] = 1
            case 3:
                seven = set(s)
                translation_map[s] = 7
            case 4:
                four = set(s)
                translation_map[s] = 4
            case 7:
                eight = set(s)
                translation_map[s] = 8
            case 5:
                two_three_five.append(s)
            case 6:
                zero_six_nine.append(s)

    for n in zero_six_nine:
        ns = set(n)
        if ns | one == eight:
            translation_map[n] = 6
        elif ns | four == eight:
            translation_map[n] = 0
        else:
            translation_map[n] = 9

    for n in two_three_five:
        ns = set(n)
        if len(ns - four) == 3:
            translation_map[n] = 2
        elif ns | one == ns:
            translation_map[n] = 3
        else:
            translation_map[n] = 5

    outputs = ["".join(sorted(o)) for o in out.strip().split(" ")]
    output = ""
    for o in outputs:
        output += str(translation_map[o])

    return int(output)


def read_input():
    with open("input") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    lines = read_input()
    print(part1(lines))
    print(part2(lines))
