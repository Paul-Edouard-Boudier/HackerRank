n = int(input())
s = set(map(int, input().split()))

for n in range(int(input())):
    l = input().split()
    getattr(s, l[0])(int(l[1])) if len(l) > 1 else getattr(s, l[0])()

print(sum(s))