#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def array_manipulation(n, queries):
    """
    ----- PARAMS -----
    @param n:   int
        must build an arrays of zeros of length n
        with indexes starting at 1
            ex: [0, 0, 0, 0] if n = 4
    @param queries: array
        what we need to add and at what index
            ex: [1, 2, 5]
             means that from index 1 to 2 included, we need
             to add 5 to the array
    @return: higher total of the array after calculation
    """
    n_arr = [0 for _ in range(n)]
    for query in queries:
        for i in range(query[0], query[1]+1):
            n_arr[i-1] += query[2]

    return max(n_arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    # n = 10
    # queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
    # print(array_manipulation(n, queries))
    result = array_manipulation(n, queries)

    fptr.write(str(result) + '\n')
    fptr.close()
