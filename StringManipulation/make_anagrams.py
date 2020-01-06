from collections import defaultdict


def make_anagram(a, b):
    dia = defaultdict(int)
    dib = defaultdict(int)
    for i in a:
        dia[i] += 1
    for i in b:
        dib[i] += 1
    count = 0
    az = 'abcdefghijklmnopqrstuvwxyz'
    for i in az:
        count += abs(dia[i] - dib[i])
    return count


if __name__ == '__main__':
    with open("testCase/make_anagrams.txt") as f:
        content = f.read()
    index1, index2 = content.split("\n")
    print(make_anagram(index1, index2))
