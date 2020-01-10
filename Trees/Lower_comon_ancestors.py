class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lca(root, v1, v2):
    if v1 > v2:
        temp = v1
        v1 = v2
        v2 = temp
    while True:
        if v1 <= root.info <= v2:
            return root
        elif v1 < v2 < root.info:
            root = root.left
        elif root.info < v1 < v2:
            root = root.right


if __name__ == '__main__':
    tree = BinarySearchTree()
    with open("TestCase/lca.txt") as f:
        num = int(f.readline())
        arr = list(map(int, f.readline().split(" ")))
        for i in range(num):
            tree.create(arr[i])
        v1, v2 = map(int, f.readline().split(" "))
    ans = lca(tree.root, v1, v2)
    print(ans)
