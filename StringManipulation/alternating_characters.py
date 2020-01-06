def alternating_characters(s):
    temp = s[0]
    res = 0
    for i in s[1:]:
        if i == temp:
            res += 1
        else:
            temp = i
    return res


if __name__ == '__main__':
    with open("testCase/alternating_characters.txt") as f:
        f.readline()
        li = f.read().split("\n")
    for st in li:
        print(alternating_characters(st))