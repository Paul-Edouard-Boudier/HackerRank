def average(array):
    m = set(array)
    return sum(m)/len(m)

if __name__ == '__main__':
    (input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
