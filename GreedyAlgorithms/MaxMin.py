def maxMin(k, arr):
    arr.sort()
    length = len(arr)
    res = arr[k-1] - arr[0]
    current = 1
    while current + k - 1 < length:
        temp = arr[current+k-1] - arr[current]
        if temp < res:
            res = temp
        current += 1
    return res


if __name__ == '__main__':
    with open("testCase/MaxMin.txt") as f:
        array = []
        num = int(f.readline().strip())
        select = int(f.readline().strip())
        for _ in range(num):
            array.append(int(f.readline().strip()))
    result = maxMin(select, array)
    print(result)
