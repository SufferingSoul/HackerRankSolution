
def minimum_absolute_difference(arr):
    sortedarr = sorted(arr)
    res = abs(sortedarr[0]-sortedarr[1])
    current = sortedarr[1]
    for i in sortedarr[2:]:
        temp = abs(current - i)
        current = i
        if temp < res:
            res = temp
    return res


if __name__ == '__main__':
    with open("testCase/MinimumAbsoluteDifference.txt") as f:
        num = int(f.readline().strip())
        array = list(map(int, f.readline().strip().split(" ")))
print(minimum_absolute_difference(array))
