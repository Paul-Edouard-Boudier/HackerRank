from collections import Counter

if __name__ == '__main__':
    s = ''.join(sorted(input()))
    result = Counter(s).most_common()[:3]
    [print(x, y) for x, y in result]