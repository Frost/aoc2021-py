from day4 import *


from io import StringIO
raw_test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

# test_input = format_input(raw_test_input.splitlines(keepends=False))
test_input = []


class TestBoard:
    test_str = """
        1  2  3  4  5
        6  7  8  9 10
        11 12 13 14 15
        16 17 18 19 20
        21 22 23 24 25
    """

    def test_from_str__reads_a_board(self):
        board = Board.from_str(self.test_str)
        assert len(board.rows) == 5
        assert len(board.cols) == 5
        assert [n.n for n in board.rows[1]] == [ 1,  2,  3,  4,  5]
        assert [n.n for n in board.rows[2]] == [ 6,  7,  8,  9, 10]
        assert [n.n for n in board.rows[3]] == [11, 12, 13, 14, 15]
        assert [n.n for n in board.rows[4]] == [16, 17, 18, 19, 20]
        assert [n.n for n in board.rows[5]] == [21, 22, 23, 24, 25]
        assert [n.n for n in board.cols[1]] == [ 1,  6, 11, 16, 21]
        assert [n.n for n in board.cols[2]] == [ 2,  7, 12, 17, 22]
        assert [n.n for n in board.cols[3]] == [ 3,  8, 13, 18, 23]
        assert [n.n for n in board.cols[4]] == [ 4,  9, 14, 19, 24]
        assert [n.n for n in board.cols[5]] == [ 5, 10, 15, 20, 25]

    def test_has_row_bingo(self):
        board = Board.from_str(self.test_str)

        assert not board.has_row_bingo()
        assert not board.has_bingo()

        for n in board.rows[1]:
            n.marked = True

        assert board.has_row_bingo()
        assert board.has_bingo()

    def test_has_col_bingo(self):
        board = Board.from_str(self.test_str)

        assert not board.has_col_bingo()
        assert not board.has_bingo()

        for n in board.cols[1]:
            n.marked = True

        assert board.has_col_bingo()
        assert board.has_bingo()

def test_part1():
    problem_input = read_input(StringIO(raw_test_input))
    assert part1(problem_input) == 4512


def test_part2():
    problem_input = read_input(StringIO(raw_test_input))
    assert part2(problem_input) == 1924
