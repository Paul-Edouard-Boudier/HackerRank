from itertools import groupby

s = input()

print(' '.join('({}, {})'.format(len(list(g)), k) for k, g in groupby(s)))
