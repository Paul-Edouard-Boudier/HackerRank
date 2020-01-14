def symmetric_differences(a, b):
    """
    @param a: enumerable
    @param b: enumerable
    @return:
    """
    l = [x for x in a.difference(b)] + [x for x in b.difference(a)]
    l.sort()
    for i in l:
        print(i)


if __name__ == '__main__':
    n = int(input())
    n_set = set(list(map(int, input().split())))
    m = int(input())
    m_set = set(list(map(int, input().split())))
    symmetric_differences(n_set, m_set)

