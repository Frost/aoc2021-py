
from icecream import ic


Coordinate = tuple[int,int]


class CaveSystem:
    dots: set[Coordinate]

    def __init__(self, dots) -> None:
        self.dots = set()
        for dot in dots:
            x,y = map(int,dot.split(","))
            self.dots.add((x,y))

    def fold_y(self, k):
        new_dots = set()
        for (x,y) in self.dots:
            new_y = k - (y - k) if y > k else y
            new_dots.add((x, new_y))

        self.dots = new_dots

    def fold_x(self, k):
        new_dots = set()
        for (x,y) in self.dots:
            new_x = k - (x - k) if x > k else x
            new_dots.add((new_x, y))

        self.dots = new_dots

    def fold(self, instruction: str):
        instruction = instruction.replace("fold along ", "")
        x_or_y, value = instruction.split("=")
        match x_or_y:
            case "x":
                self.fold_x(int(value))
            case "y":
                self.fold_y(int(value))

    def __len__(self):
        return len(self.dots)

    def __str__(self) -> str:
        max_x = 0
        max_y = 0
        for (x,y) in self.dots:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

        matrix = []
        for y in range(max_y + 1):
            matrix.append( ["."] * (max_x + 1) )

        for (x,y) in self.dots:
            matrix[y][x] = "#"

        return ("\n".join(["".join(row) for row in matrix]))



def part1(dots, folds):
    cave = CaveSystem(dots)
    fold = folds[0]

    cave.fold(fold)
    answer = len(cave)

    return answer


def part2(dots, folds):
    cave = CaveSystem(dots)
    for fold in folds:
        cave.fold(fold)

    print(cave)


def parse_input(data: str) -> tuple[list[str], list[str]]:
    dots, folds = data.split("\n\n")
    return dots.split("\n"), folds.split("\n")


def read_input() -> tuple[list[str], list[str]]:
    with open("input") as f:
        data = f.read().strip()
        return parse_input(data)


if __name__ == "__main__":
    dots, folds = read_input()
    print(part1(dots, folds))
    print(part2(dots, folds))
