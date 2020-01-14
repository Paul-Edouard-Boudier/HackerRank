import string

def print_rangoli(size):
    """
    width of pattern = (size-1) * 4 + 1
    height of pattern = size
    """
    if size > 27 or size < 0:
        return False

    width = ((size-1) * 4) + 1
    char = list(string.ascii_lowercase)[:size]

    reverse = char
    reverse.reverse()
    print('')
    for i in range(size + 1):
        if i is 1:
            continue
        if i is not 0:
            l = reverse[:i]
            temp = char[:i-1]
            temp.reverse()
            l.extend(temp)
            print("{:-^{width}s}".format("-".join(l), width=width))
        else:
            l = reverse[i]
            print("{:-^{width}s}".format(l, width=width))

    for i in range(size, 0, -1):
        if i is size:
            continue

        if i is not 0:
            l = char[:i]
            temp = reverse[:i-1]
            temp.reverse()
            l.extend(temp)
            print("{:-^{width}s}".format("-".join(l), width=width))
        else:
            print("{:-^{width}s}".format(char[i], width=width))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
