from __future__ import annotations

from icecream import ic
from collections import Counter, defaultdict, deque

import icecream


class Node:
    name: str
    neighbors: set["Node"]

    def __init__(self, name) -> None:
        self.name = name
        self.neighbors = set()

    @property
    def large(self) -> bool:
        return self.name[0].isupper()

    @property
    def small(self) -> bool:
        return self.name[0].islower()

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"<Node {self.name}>"


Graph = dict[str, Node]


class TreeNode:
    parent: TreeNode | None
    name: str
    path: list[str]

    def __init__(self, parent, name) -> None:
        self.parent = parent
        self.name = name
        self.path = parent.path + [name] if parent else [name]

    def allows_child(self, key: str) -> bool:
        return key not in filter(str.islower, self.path)

    def allows_child_with_single_duplicate(self, key: str) -> bool:
        small = filter(str.islower, self.path)
        small = list(small)
        counts = defaultdict(int)
        for c in small:
            counts[c] += 1
            if counts[c] > 1:
                return key not in small

        return True

    def __repr__(self) -> str:
        return f"<TreeNode {self.name}>"


def make_graph(edges) -> Graph:
    nodes: dict[str,Node] = dict()

    for edge in edges:
        start_key, end_key = edge.split("-")
        start = nodes.get(start_key, Node(name=start_key))
        end = nodes.get(end_key, Node(name=end_key))

        if end_key != "start":
            start.neighbors.add(end)
        if start_key != "start":
            end.neighbors.add(start)

        nodes[start_key] = start
        nodes[end_key] = end

    return nodes


def traverse(graph: Graph, allow_fun=TreeNode.allows_child):
    stack: deque[TreeNode] = deque()

    root = TreeNode(parent=None, name="start")

    for n in graph["start"].neighbors:
        stack.append(TreeNode(root, n.name))
    while stack:
        tree: TreeNode = stack.pop()

        if tree.name == "end":
            yield 1
        else:
            node = graph[tree.name]
            for n in node.neighbors:
                if allow_fun(tree, n.name):
                    child = TreeNode(tree, n.name)
                    stack.append(child)


def part1(lines) -> int:
    graph = make_graph(lines)
    paths = list(traverse(graph))
    return len(paths)


def part2(lines):
    graph = make_graph(lines)
    return sum(traverse(graph, TreeNode.allows_child_with_single_duplicate))


def read_input():
    with open("input") as f:
        return map(str.strip, f.readlines())


if __name__ == "__main__":
    print(part1(read_input()))
    print(part2(read_input()))
