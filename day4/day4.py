from __future__ import annotations
import re
from dataclasses import dataclass

from icecream import ic


@dataclass
class Number:
    n: int
    row: int
    col: int
    marked: bool = False


class Board:
    numbers: dict[int,Number]
    rows: dict[int,list[Number]]
    cols: dict[int,list[Number]]

    def __init__(self) -> None:
        self.rows = {1: [], 2: [], 3: [], 4: [], 5: []}
        self.cols = {1: [], 2: [], 3: [], 4: [], 5: []}
        self.numbers = dict()

    @staticmethod
    def from_str(raw_board) -> Board:
        board = Board()
        for row, numbers in enumerate(raw_board.strip().split("\n"), start=1):
            numbers = numbers.strip()
            for col, number in enumerate(re.split(r" +", numbers), start=1):
                n = int(number)
                number = Number(n=n, marked=False, row=row, col=col)
                board.numbers[n] = number
                board.rows[row].append(number)
                board.cols[col].append(number)

        return board

    def has_bingo(self) -> bool:
        return self.has_row_bingo() or self.has_col_bingo()

    def has_row_bingo(self) -> bool:
        for row in self.rows.values():
            if all(n.marked for n in row):
                return True
        return False

    def has_col_bingo(self) -> bool:
        for col in self.cols.values():
           if all(n.marked for n in col):
               return True
        return False

    def mark(self, num) -> None:
        if number := self.numbers.get(num):
            number.marked = True

    def __repr__(self) -> str:
        out = ""
        for row in self.rows.values():
            for num in row:
                if num.marked:
                    out += "X ".rjust(3)
                else:
                    out += f"{num.n} ".rjust(3)
            out += "\n"

        return out


class BingoGame:
    boards: dict[int,Board] = []

    def __init__(self, boards) -> None:
        self.boards = {i:board for i, board in enumerate(boards, 1)}

    def tick(self, number):
        winning_boards = []
        for i, board in self.boards.items():
            board.mark(number)
            if board.has_bingo():
                winning_boards.append((i, board))

        for i, _board in winning_boards:
            self.boards.pop(i)

        return winning_boards

def part1(problem_input) -> int:
    numbers, boards = problem_input
    game = BingoGame(boards)

    for number in numbers:
        if board := game.tick(number):
            board = board[0][1]
            unmarked_numbers = [n.n for n in board.numbers.values() if not n.marked]
            return sum(unmarked_numbers) * number

    return 0


def part2(problem_input):
    numbers, boards = problem_input
    game = BingoGame(boards)

    last_board_to_win = None
    last_number_to_win = -1
    for number in numbers:
        if board := game.tick(number):
            last_board_to_win = board
            last_number_to_win = number
        if len(game.boards) == 0:
            break

    if last_board_to_win is not None:
        _board_number, board = last_board_to_win[0]
        unmarked_numbers = [n.n for n in board.numbers.values() if not n.marked]
        return sum(unmarked_numbers) * last_number_to_win
    return 0


def read_input(input = None) -> tuple[list[int], list[Board]]:
    def format_numbers(line):
        return list(map(int, line.strip().split(",")))

    def format_boards(boards):
        return boards.strip().split("\n\n")

    if input is not None:
        random_numbers = format_numbers(input.readline())
        raw_boards = format_boards(input.read())
    else:
        with open("input") as f:
            random_numbers = format_numbers(f.readline())
            raw_boards = format_boards(f.read())

    boards = [Board.from_str(b) for b in raw_boards]

    return (random_numbers, boards)


if __name__ == "__main__":
    input = read_input()
    print(part1(input))
    print(part2(input))
