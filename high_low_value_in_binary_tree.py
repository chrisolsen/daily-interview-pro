"""
Hi, here's your problem today. This problem was recently asked by Apple:
    Given an integer k and a binary search tree, find the floor (less than or
    equal to) of k, and the ceiling (larger than or equal to) of k. If either
    does not exist, then print them as None.
Here is the definition of a node for the tree.
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(node, k, floor=None, ceil=None):
    # first call only
    if ceil is None and node.value > k:
        ceil = node.value
    if floor is None and node.value < k:
        floor = node.value

    # second and later calls
    if ceil is not None and node.value < ceil and node.value > k:
        ceil = node.value
    if floor is not None and node.value > floor and node.value < k:
        floor = node.value

    if node.left is not None:
        floor, ceil = findCeilingFloor(node.left, k, floor, ceil)
    if node.right is not None:
        floor, ceil = findCeilingFloor(node.right, k, floor, ceil)

    return (floor, ceil)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.left.left = Node(7)
    root.left.left.left = Node(1)
    root.left.left.right = Node(16)
    root.left.right = Node(9)
    root.right = Node(13)
    root.right.left = Node(3)
    root.right.right = Node(3)
    assert findCeilingFloor(root, 5) == (3, 7)
    assert findCeilingFloor(root, 12) == (10, 13)
    assert findCeilingFloor(root, 3) == (2, 7)
