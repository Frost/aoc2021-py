
from .day12 import *

small_sample_input = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

medium_sample_input = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

large_sample_input = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


def test_make_graph():
    graph = make_graph([
        "start-A",
        "A-end",
        "start-b",
    ])

    assert set([n.name for n in graph["start"].neighbors]) == set(["A", "b"])

def test_tree_node_allows_child():
    root = TreeNode(None, "start")
    child = TreeNode(root, "a")
    grandchild = TreeNode(child, "a")

    assert not root.allows_child("start")

    assert root.allows_child("a")
    assert not child.allows_child("a")
    assert not grandchild.allows_child("a")

    assert root.allows_child_with_single_duplicate("a")
    assert child.allows_child_with_single_duplicate("a")
    assert not grandchild.allows_child_with_single_duplicate("a")

    g2child = TreeNode(grandchild, "b")
    assert g2child.allows_child("A")
    assert not g2child.allows_child("a")
    assert not g2child.allows_child("b")


def test_part1():
    assert part1(small_sample_input.strip().split("\n")) == 10
    assert part1(medium_sample_input.strip().split("\n")) == 19
    assert part1(large_sample_input.strip().split("\n")) == 226


def test_part2():
    assert part2(small_sample_input.strip().split("\n")) == 36
    assert part2(medium_sample_input.strip().split("\n")) == 103
    assert part2(large_sample_input.strip().split("\n")) == 3509
