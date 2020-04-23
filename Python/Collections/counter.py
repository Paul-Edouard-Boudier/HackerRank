from collections import Counter

_ = int(input())
list_ = Counter([int(x) for x in input().split()])
n, total = int(input()), 0
for _ in range(n):
    size, price = [int(x) for x in input().split()]
    if list_[size] > 0:
        total += price
        list_.subtract({size})
    
print(total)