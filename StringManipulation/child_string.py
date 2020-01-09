from collections import defaultdict
import numpy as np


def common_child(s1, s2):
    le = len(s1)
    rect = np.zeros((le, le))
    for i in range(le):
        if s1[i] == s2[0]:
            rect[0, i] = 1
        elif s2[i] == s1[0]:
            rect[i, 0] = 1
        else:
            if i > 0:
                rect[i, 0] = rect[i-1, 0]
                rect[0, i] = rect[0, i-1]
    for i in range(1, le):
        for j in range(1, le):
            if s2[i] == s1[j]:
                rect[i, j] = rect[i-1, j-1] + 1
            else:
                rect[i, j] = max(rect[i, j-1], rect[i-1, j])
    return rect[le-1, le-1]


def common_child(s1, s2):
    le = len(s1)
    rect = [[0 for _ in range(le)] for _ in range(le)]
    for i in range(le):
        if s1[i] == s2[0]:
            rect[0][i] = 1
        elif s2[i] == s1[0]:
            rect[i][0] = 1
        else:
            if i > 0:
                rect[i][0] = rect[i-1][0]
                rect[0][i] = rect[0][i-1]
    for i in range(1, le):
        for j in range(1, le):
            if s2[i] == s1[j]:
                rect[i][j] = rect[i-1][j-1] + 1
            else:
                rect[i][j] = max(rect[i][j-1], rect[i-1][j])
    return rect[le-1][le-1]


if __name__ == '__main__':
    with open("testCase/common_string.txt") as f:
        a, b = f.read().split("\n")
    print(int(common_child(a, b)))
