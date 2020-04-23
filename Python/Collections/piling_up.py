t = int(input())

for i in range(t):
    n, pile, r = int(input()), [], True
    cubes_list = [int(x) for x in input().split()]
    while cubes_list:
        x, y = cubes_list[0], cubes_list[-1]
        if x > y:
            if pile and pile[-1] < x:
                r = False
                break
            pile.append(x)
            del cubes_list[0]
        else:
            if pile and pile[-1] < y:
                r = False
                break
            pile.append(y)
            del cubes_list[-1]
    print("No" if r is False else "Yes")
