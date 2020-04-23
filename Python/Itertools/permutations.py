from itertools import permutations

s, k = input().split()
print(*["".join(el) for el in list(permutations(sorted(s), int(k)))], sep='\n')
