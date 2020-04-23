from collections import OrderedDict

result = OrderedDict()
n = int(input())
for _ in range(n):
    p = input().split()
    name = " ".join(p[:-1])
    price = int(p[-1])
    result[name] = price if name not in result else result[name] + price
    
[print(i, result[i]) for i in result]