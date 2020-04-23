import itertools

a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]

result = list(itertools.product(a, b))
print(' '.join('({}, {})'.format(*el) for el in result))
