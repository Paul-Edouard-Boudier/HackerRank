#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglass_sum(arr: list) -> int:
    """
    Calculate the highest sum of the hourglasses inside arr
    check: https://www.hackerrank.com/challenges/2d-array/problem

    ----- PARAMS -----
    @param arr:     list
            2d array representing a cube

    @return: highest sum of hourglass of the array __arr__
    """
    sum_list = []
    for i in range(4):
        for a in range(4):
            # sum = 0
            sub_list = arr[i][a:(a+3)]
            sub_list.append(arr[i+1][a+1])
            sub_list.extend(arr[i+2][a:(a+3)])

            sum_list.append(sum(sub_list))
    return max(sum_list)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # arr = []
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]

    result = hourglass_sum(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()

