for _ in range(int(input())):
    la,a,lb,b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))
