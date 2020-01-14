def print_formatted(number):
    maxwidth = len('{0:b}'.format(number))

    for i in range(0, number):
        line = '{0: >{maxwidth}d} {0: >{maxwidth}o} {0: >{maxwidth}X} {0: >{maxwidth}b}'\
            .format(i, maxwidth=maxwidth)

        print(line)

if __name__ == '__main__':
    n = 2
    print_formatted(n)
