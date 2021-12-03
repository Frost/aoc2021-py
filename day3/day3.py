from dataclasses import dataclass
from icecream import ic


@dataclass
class Power:
    gamma: int
    epsilon: int


def part1(input_lines):
    power = calculate_power(input_lines)

    return power.gamma * power.epsilon


def calculate_power(input_lines, equal_is: int = 1):
    counts = list()

    for line in input_lines:
        for index, char in enumerate(line.strip()):
            if len(counts) <= index:
                counts.append({0: 0, 1: 0})

            counts[index][int(char)] += 1

    power = Power(gamma=0, epsilon=0)

    gamma = []
    epsilon = []
    for count in counts:
        gamma_key = 0 if count[0] > count[1] else 1
        epsilon_key = 1 if gamma_key == 0 else 0

        gamma.append(gamma_key)
        epsilon.append(epsilon_key)

    power.gamma = int("".join(map(str, gamma)), 2)
    power.epsilon = int("".join(map(str, epsilon)), 2)

    return power


def filter_rating(lines, rating_key):
    zfill = len(lines[0].strip())
    power = calculate_power(lines)

    power_string = f"{getattr(power, rating_key):b}".zfill(zfill)

    prefix = ""
    for i in range(len(power_string)):
        prefix += power_string[i]
        lines = [line for line in lines if line.startswith(prefix)]
        power = calculate_power(lines)
        power_string = f"{getattr(power, rating_key):b}".zfill(zfill)

        if len(lines) == 1:
            return int(lines[0], 2)


def part2(input_lines):
    oxygen_rating = filter_rating(input_lines, "gamma")
    ic(oxygen_rating)
    co2_scrubber_rating = filter_rating(input_lines, "epsilon")
    ic(co2_scrubber_rating)

    return oxygen_rating * co2_scrubber_rating


if __name__ == "__main__":
    with open("input") as f:
        input_lines = f.readlines()

    print(part1(input_lines))
    print(part2(input_lines))
