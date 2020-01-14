def mod_pow(x: int, y: int, m: int):
    """
    """
    if 0 < x > 10:
        return False
    if 0 < y > 10:
        return False
    if 1 < m > 1000:
        return False
    print(pow(x,y))
    print(pow(x,y,m))



if __name__ == '__main__':
    x, y, m = int(input()), int(input()), int(input())
    mod_pow(x, y, m)
