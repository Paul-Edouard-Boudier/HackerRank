def mod_divmod(x: int, y: int):
    """
    """
    print(x//y)
    print(x%y)
    print(divmod(x,y))



if __name__ == '__main__':
    x, y = int(input()), int(input())
    mod_divmod(x, y)
