
import pytest
from day10 import *


test_input = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


@pytest.mark.parametrize(
    "line,illegal_char",
    (
        ("[]", None),
        ("()", None),
        ("{}", None),
        ("<>", None),
        ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
        ("[[<[([]))<([[{}[[()]]]", ")"),
        ("[{[{({}]{}}([{[{{{}}([]", "]"),
        ("[<(<(<(<{}))><([]([]()", ")"),
        ("<{([([[(<>()){}]>(<<{{", ">"),
    )
)
def test_illegal_characters(line, illegal_char):
    assert parse_line(line) == illegal_char


@pytest.mark.parametrize(
    "line,completion",
    (
        ("({", "})"),
        ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
        ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
        ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
        ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>"),
        ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>"),
    )
)
def test_complete_line(line, completion):
    assert "".join(complete_line(line)) == completion


@pytest.mark.parametrize(
    "completion,score",
    (
        ("}}]])})]", 288957),
        (")}>]})", 5566),
        ("}}>}>))))", 1480781),
        ("]]}}]}]}>", 995444),
        ("])}>", 294),
    )
)
def test_score_completion(completion, score):
    assert score_completion(completion) == score


def test_part1():
    lines = test_input.strip().split("\n")
    assert part1(lines) == 26397


def test_part2():
    lines = test_input.strip().split("\n")
    assert part2(lines) == 288957
