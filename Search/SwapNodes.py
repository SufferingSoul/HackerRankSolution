import sys
sys.setrecursionlimit(2000)


class BinaryNode:
    def __init__(self, v, d=-1, l=-1, r=-1):
        self.value = v
        self.left = l
        self.right = r
        self.deep = d

    def set_left_child(self, v):
        self.left = v

    def set_right_child(self, v):
        self.right = v


def travel(node, res):
    if node.value == -1:
        return
    travel(node.left, res)
    res.append(node.value)
    travel(node.right, res)


def swap(node, deep):
    if node.value == -1:
        return
    if node.deep % deep == 0:
        temp = node.left
        node.left = node.right
        node.right = temp
    swap(node.left, deep)
    swap(node.right, deep)


def swapNodes(indexes, queries):
    head = BinaryNode(1, 1)
    queue = [head]
    out = []
    for node in indexes:
        current = queue.pop(0)
        current.set_left_child(BinaryNode(node[0], current.deep + 1))
        current.set_right_child(BinaryNode(node[1], current.deep + 1))
        if node[0] != -1:
            queue.append(current.left)
        if node[1] != -1:
            queue.append(current.right)
    for d in queries:
        swap(head, d)
        res = []
        travel(head, res)
        out.append(res)
    return out



if __name__ == '__main__':
    treenode = []
    query = []
    deep = []
    with open("TestCase/case1.txt") as f:
        n = int(f.readline().strip())
        for _ in range(n):
            li = list(map(int, f.readline().split(" ")))
            treenode.append(li)
        m = int(f.readline().strip())
        for _ in range(m):
            query.append(int(f.readline().strip()))
    print(treenode, query)
    result = swapNodes(treenode, query)
    print(result)