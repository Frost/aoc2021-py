from dataclasses import dataclass


@dataclass
class Location:
    depth = 0
    distance = 0
    aim = 0


def part1(input_lines):
    location = Location()

    for line in input_lines:
        command, value = line.split(" ")
        value = int(value)
        match command:
            case "up":
                location.depth -= value
            case "down":
                location.depth += value
            case "forward":
                location.distance += value

    return location.depth * location.distance


def part2(input_lines):
    location = Location()

    for line in input_lines:
        command, value = line.split(" ")
        value = int(value)
        match command:
            case "up":
                location.aim -= value
            case "down":
                location.aim += value
            case "forward":
                location.distance += value
                location.depth += location.aim * value

    return location.depth * location.distance


if __name__ == "__main__":
    with open("input") as f:
        input_lines = f.readlines()

    print(part1(input_lines))
    print(part2(input_lines))
