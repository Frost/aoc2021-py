
from dataclasses import dataclass
from icecream import ic


class Octopus:
    energy_level: int
    x: int
    y: int

    def __init__(self, x: int, y: int, energy_level: int) -> None:
        self.x = x
        self.y = y
        self.energy_level = energy_level

    @property
    def neighbors(self):
        x, y = self.x, self.y
        return [
            (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y),                 (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
        ]

    @property
    def coordinate(self):
        return (self.x, self.y)

    def brighten(self):
        self.energy_level += 1

    def blacken(self):
        self.energy_level = 0

    @property
    def will_flash(self):
        return self.energy_level > 9


class Cave:
    matrix: list[list[Octopus]]

    def __init__(self, matrix_lines):
        self.matrix = []
        for y, line in enumerate(matrix_lines):
            row = []
            for x, e in enumerate(line.strip()):
                octopus = Octopus(x=x, y=y, energy_level=int(e))
                row.append(octopus)

            self.matrix.append(row)


    def __getitem__(self, coordinate) -> Octopus:
        x, y = coordinate
        return self.matrix[y][x]


    def tick(self) -> int:
        # 1. increase all energy levels
        flashing_octopi = self.brighten_all_octopi()

        # 2. resolve flashes
        flashed_octopi = self.resolve_flashes(flashing_octopi)

        # 3. set all flashed coordinates to 0
        for coordinate in flashed_octopi:
            self[coordinate].blacken()

        return len(flashed_octopi)

    def brighten_all_octopi(self) -> set:
        flashing_octopi = set()
        for row in self.matrix:
            for octopus in row:
                octopus.brighten()
                if octopus.will_flash:
                    flashing_octopi.add(octopus.coordinate)

        return flashing_octopi

    def resolve_flashes(self, flashing_octopi) -> set:
        flashed_octopi = set()
        while len(flashing_octopi - flashed_octopi) > 0:
            for coordinate in flashing_octopi - flashed_octopi:
                flashed_octopi.add(coordinate)

                for neighbor in self[coordinate].neighbors:
                    if self.valid_coordinate(neighbor):
                        self[neighbor].brighten()
                        if self[neighbor].will_flash:
                            flashing_octopi.add(neighbor)

        return flashed_octopi

    def valid_coordinate(self, coordinate):
        x, y = coordinate
        return 0 <= x < len(self.matrix[0]) and 0 <= y < len(self.matrix)

    def energy_levels(self):
        out = []
        for row in self.matrix:
            out.append([o.energy_level for o in row])

        return out

    def __len__(self):
        return sum([len(row) for row in self.matrix])



def part1(lines):
    cave = Cave(lines)
    flashes = 0
    for i in range(100):
        flashes += cave.tick()

    return flashes


def part2(lines):
    cave = Cave(lines)

    step = 0
    while True:
        flashes = cave.tick()
        step += 1
        if flashes == len(cave):
            return step


def read_input():
    with open("input") as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input()
    print(part1(lines))
    print(part2(lines))
