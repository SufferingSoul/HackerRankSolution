class TreeNode:
    def __init__(self, value, order,):
        self.value = value
        self.order = order
        self.parent = None
        self.children = []


def build_tree(c, edges):
    root = TreeNode(c[0], 1)
    for s,t in edges:
        pass



def balanced_trees(c, edges):
    print(c)
    print(edges)


if __name__ == '__main__':
    with open("TestCase/balanced_trees.txt") as f:
        n = int(f.readline().strip())
        cs = []
        edges = []
        for i in range(n):
            num = int(f.readline())
            c = list(map(int, f.readline().strip().split(" ")))
            cs.append(c)
            edge = []
            for j in range(num - 1):
                edge.append(list(map(int, f.readline().strip().split(" "))))
            edges.append(edge)
    for i in zip(cs, edges):
        balanced_trees(i[0], i[1])
