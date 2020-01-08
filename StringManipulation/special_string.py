def sub_str_count(num, str):
    count = num
    for i in range(1, num):
        current = str[i-1]
        lower, middle, high = i-1, i, i+1
        while lower >= 0 and high < num:
            if str[lower] == str[high] == current:
                count += 1
                # print(str[lower:high + 1])
                lower -= 1
                high += 1
            else:
                break
        while middle < num:
            if current == str[middle-1] == str[middle]:
                count += 1
                # print(str[middle-1:middle+1])
                middle += 2
            else:
                break
    return count


if __name__ == '__main__':
    with open("testCase/sub_str_count.txt") as f:
        n = int(f.readline().strip("\n"))
        s = f.readline().strip("\n")
    print(sub_str_count(n, s))
