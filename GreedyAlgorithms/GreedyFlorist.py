def get_minimum_ost(k, c):
    c.sort()
    res = 0
    level = 1
    while len(c) > k:
        res += sum(c[len(c) - k:]) * level
        level += 1
        c = c[:len(c) - k]
    res += sum(c) * level
    return res


if __name__ == '__main__':
    with open("testCase/GreedyFlorist.txt") as f:
        n, k = list(map(int, f.readline().strip().split(" ")))
        c = list(map(int, f.readline().strip().split(" ")))
    res = get_minimum_ost(k, c)
    print(res)
