for i in range(int(input())):
    try:
        ints = [int(x) for x in input().split()]
        print(int(ints[0] / ints[1]))
    except ValueError as e:
        print(f'Error code: {e}')
    except ZeroDivisionError as e:
        print(f'Error code: integer division or modulo by zero')