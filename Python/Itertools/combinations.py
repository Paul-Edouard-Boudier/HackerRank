from itertools import combinations

s, k = input().split()
for i in range(int(k)):
    print(*["".join(el) for el in combinations(sorted(s), i+1)], sep="\n")
