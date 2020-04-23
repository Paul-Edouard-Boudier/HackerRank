from itertools import combinations

len_ = int(input())
list_ = [x for x in input().split()]
r = int(input())

combi = list(combinations(list_, r))

stats = ['a' for el in combi if 'a' in el]
print(len(stats)/len(combi))
