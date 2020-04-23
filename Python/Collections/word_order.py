from collections import OrderedDict

words, n = OrderedDict(), int(input())

for _ in range(n):
    w = input()
    words[w] = 1 if w not in words else words[w] + 1

print(len(words))
print(" ".join([str(words[i]) for i in words]))