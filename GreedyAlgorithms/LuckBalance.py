def luck_balance(k, contests):
    luck = 0
    imt = []
    for te in contests:
        if te[1] == 0:
            luck += te[0]
        else:
            luck += te[0]
            imt.append(te[0])
    if len(imt) <= k:
        return luck
    else:
        red = sorted(imt)[:len(imt)-k]
        luck -= 2*sum(red)
    return luck


if __name__ == '__main__':
    contest = []
    with open("testCase/LuckBalance.txt") as f:
        n, k = map(int, f.readline().strip().split(" "))
        for _ in range(n):
            contest.append(list(map(int, f.readline().strip().split(" "))))
    res = luck_balance(k, contest)
    print(res)
