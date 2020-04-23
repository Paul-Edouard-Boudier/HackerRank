# SOLUTION 1 #
# 4 lines or less, said the challenge

n, total, index = [int(input()), 0, input().split().index('MARKS')]
for i in range(n):
    total += int(input().split()[index])
print(total/n)