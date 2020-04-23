from collections import defaultdict

k = int(input())
l = [int(x) for x in input().split()]
t = defaultdict(int)
for x in l:
    t[x] += 1

[print(i) for i in t if t[i] is 1]

# didn't use the set tools here because the problem is somewhat obivious without it,
# but with it, it becomes a math problem 

# HERE solution for math problem (from hackerranck site)
k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))

# We simply calculate the difference in what the sum would be if there were K elements of all groups. 
# We will have k-1*captains room number left, we simply didve by k-1 to get the answer.