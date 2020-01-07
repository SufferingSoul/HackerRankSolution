from collections import defaultdict


def isvalid(s):
    di = defaultdict(int)
    for i in s:
        di[i] += 1
    dicount = defaultdict(int)
    for i in di.values():
        dicount[i] += 1
    keys = list(dicount.keys())
    if len(keys) == 1:
        return 'YES'
    elif len(keys) > 2:
        return 'NO'
    elif min(keys) == 1 and dicount[min(keys)] == 1:
        return 'YES'
    elif dicount[max(keys)] * (max(keys)-min(keys)) > 1:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    with open("testCase/valid_string.txt") as f:
        st = f.read().strip("\n")
    print(isvalid(st))
