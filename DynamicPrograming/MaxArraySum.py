def maxSubsetSum(arr):
    result = list()
    result.append(arr[0] if arr[0] > 0 else 0)
    result.append(max(result[0], arr[1]))
    for i in range(2, len(arr)):
        result.append(max((arr[i]+result[i-2]), result[i-1], 0))
    return result[-1]


if __name__ == '__main__':
    input_str = open("testCase/testCase.txt")
    num = int(input_str.readline())
    num_list = list(map(int, input_str.readline().split(" ")))
    print(maxSubsetSum(num_list))
