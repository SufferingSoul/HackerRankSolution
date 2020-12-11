-- coding: utf-8 --
def checkBST(root):
    return check(root, -1, 10001)


def check(node, minum, maxum):
    if node is None:
        return True
    if node.data >= maxum or node.data <= minum:
        return False
    return check(node.left, minum, node.data) and check(node.right, node.data, maxum)

