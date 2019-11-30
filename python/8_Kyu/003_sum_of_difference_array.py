# https://www.codewars.com/kata/sum-of-differences-in-array/train/javascript

# 8 Kyu

# Your task is to sum the differences between consecutive pairs in the array in descending order.

# For example: sumOfDifferences([2, 1, 10]) Returns 9

# Descending order: [10, 2, 1]

# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

# If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell).


def sumOfDifferences(num_array):
    reversed = sorted(num_array, reverse=True)
    sum = 0
    for n in range(0, len(reversed)-1):
        sum = sum + (reversed[n] - (reversed[n+1]))
    return sum


print(sumOfDifferences([2, 1, 10]))
