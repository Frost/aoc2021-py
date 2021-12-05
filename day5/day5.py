from dataclasses import dataclass
from collections import defaultdict
from icecream import ic


@dataclass
class Coordinate:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class Line:
    start: Coordinate
    end: Coordinate

    def __init__(self, start, end) -> None:
        start_x, start_y = start.split(",")
        end_x, end_y = end.split(",")

        self.start = Coordinate(
            x=int(start_x),
            y=int(start_y)
        )
        self.end = Coordinate(
            x=int(end_x),
            y=int(end_y)
        )

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    def is_diagonal(self):
        return not(self.is_horizontal() or self.is_vertical())

    def coordinates(self):
        if self.is_horizontal():
            y = self.start.y
            if self.start.x < self.end.x:
                fro = self.start.x
                to = self.end.x + 1
            else:
                fro = self.end.x
                to = self.start.x + 1

            coordinates = []
            for x in range(fro, to):
                coordinates.append(Coordinate(x=x, y=y))
            return coordinates

        if self.is_vertical():
            x = self.start.x
            if self.start.y < self.end.y:
                fro = self.start.y
                to = self.end.y + 1
            else:
                fro = self.end.y
                to = self.start.y + 1

            coordinates = []
            for y in range(fro, to):
                coordinates.append(Coordinate(x=x, y=y))
            return coordinates

        # if diagonal
        x_step = 1 if self.start.x < self.end.x else -1
        y_step = 1 if self.start.y < self.end.y else -1

        coordinates = []
        x = self.start.x
        y = self.start.y
        while True:
            coordinates.append(Coordinate(x=x, y=y))

            if x == self.end.x and y == self.end.y:
                break

            x += x_step
            y += y_step

        return coordinates



def part1(lines):
    counts = defaultdict(int)
    overlapping_coordinates = set()
    for line in lines:
        if line.is_horizontal() or line.is_vertical():
            for coordinate in line.coordinates():
                counts[coordinate] += 1
                if counts[coordinate] > 1:
                    overlapping_coordinates.add(coordinate)

    return len(overlapping_coordinates)


def part2(lines):
    # 18571 is too low
    counts = defaultdict(int)
    overlapping_coordinates = set()
    for line in lines:
        for coordinate in line.coordinates():
            counts[coordinate] += 1
            if counts[coordinate] > 1:
                overlapping_coordinates.add(coordinate)

    return len(overlapping_coordinates)


def read_input():
    with open("input") as f:
        raw_input = f.readlines()

    return format_input(raw_input)


def format_input(raw_lines):
    lines = []
    for raw_line in raw_lines:
        start, end = raw_line.split(" -> ")
        lines.append(Line(start, end))

    return lines


if __name__ == "__main__":
    input = read_input()
    print(part1(input))
    print(part2(input))
