def happiness_level(x, a, b):
    """
    calculate a happiness level
    method is:
    for each int in x, if int in a, then + 1
    if int in b, then -1

    ----- PARAMS -----
    @param x:   array
            array of numbers
    @param a:   set
            set of numbers that we like
    @param b:   set
            set of numbers that we don't like
    @return:    int
            the sum of happiness
    """
    total = 0
    for i in x:
        total += 1 if i in a else -1 if i in b else 0
    return total


if __name__ == '__main__':
    list(map(int, input().split()))
    x = list(map(int, input().split()))
    a = set(list(map(int, input().split())))
    b = set(list(map(int, input().split())))
    #
    # x = [1, 5, 3]
    # a = [1, 3]
    # b = [5, 7]
    print(happiness_level(x, a, b))

