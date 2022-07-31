"""
    Title			: Level order print
    Description		: Level order binary tree traversal
    Author			: Md Musleh Uddin Khan
    Date			: 31-07-2022
"""


class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printCurrentLevel(root, i)


def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level order traversal of binary tree is - ", end=" ")
    printLevelOrder(root)
