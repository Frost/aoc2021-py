
from collections import deque
from pdb import set_trace
from icecream import ic


POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

MATCH = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

COMPLETION_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def is_opener(ch):
    return ch in MATCH.keys()


def parse_line(line: str):
    stack = list()
    chars = deque(line.strip())

    while len(chars) > 0:
        ch = chars.popleft()
        if is_opener(ch):
            # Any opener is ok to just push onto the stack
            stack.append(ch)
            continue

        if len(stack) == 0:
            # We got a closing character when the stack is empty
            # It is invalid, so let's return it
            return ch

        # We have a closing character, and the stack is not empty
        # Let's match the top of the stack to the new character
        top = stack[-1]
        if ch == MATCH[top]:
            # The characters match, pop the top off the stack
            stack.pop()
            continue

        # The characters don't match, we have an invalid character
        return ch

    return stack


def complete_line(line: str):
    stack = parse_line(line)

    return list(reversed([MATCH[ch] for ch in stack]))


def score_completion(completion: list):
    score = 0

    for char in completion:
        score *= 5
        score += COMPLETION_POINTS[char]

    return score


def part1(lines):
    points = []
    for line in lines:
        if (ch := parse_line(line)) and ch in MATCH.values():
            points.append(POINTS[ch])

    return sum(points)


def part2(lines):
    scores = []
    for line in lines:
        parsed = parse_line(line)
        if isinstance(parsed, str):
            continue

        completion = complete_line(line)
        line_score = score_completion(completion)
        scores.append(line_score)

    middle_score_index = len(scores) // 2
    return sorted(scores)[middle_score_index]


def read_input():
    with open("input") as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input()
    print(part1(lines))
    print(part2(lines))
