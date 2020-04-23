from collections import deque

c = deque()

for n in range(int(input())):
    l = input().split()
    getattr(c, l[0])(l[1]) if len(l) > 1 else getattr(c, l[0])()

[print(x, end=' ') for x in c]