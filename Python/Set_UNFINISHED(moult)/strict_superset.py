a = set(input().split())

for _ in range(int(input())):
    if len(set(input().split()).difference(a)) != 0:
        print(False)
        exit()

print(True)