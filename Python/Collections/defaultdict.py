from collections import defaultdict

d = defaultdict(list)
n, m = [int(x) for x in input().split()]
d = {'s': 0}
for i in range(n):
    d[str(input())].append(str(i+1))
result = []

for i in range(m):
    l = str(input())
    result.append(d[l] if l in d else ['-1'])

for i in result:
    print(" ".join(i))
