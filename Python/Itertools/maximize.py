from itertools import product

_ = [int(x) for x in input().split()]
n_list = _[0]
modulo = _[1]
all_lists = []
combs = []

for i in range(n_list):
    all_lists.append([int(x) for x in input().split()][1:])
    
combi = list(product(*all_lists))

result = []
for i in combi:
    temp = 0
    for y in i:
        temp += y**2
    result.append(temp%modulo)

print(max(result))