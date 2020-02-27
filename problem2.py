# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6]
# Follow-up: what if you can't use division?

import numpy


def my_product_of_all_numbers(data):
    """My solution. (It uses division)"""
    prod = numpy.prod(data)
    result = [0] * len(data)
    for i, value in enumerate(data):
        result[i] = prod / value

    return result


expected = [120, 60, 40, 30, 24]
assert my_product_of_all_numbers(data=[1, 2, 3, 4, 5]) == expected

expected = [2, 3, 6]
assert my_product_of_all_numbers(data=[3, 2, 1]) == expected


def gfg_product_of_all_numbers(data):
    """Solution found on the Geeks for Geeks site. (It does not use division)"""
    """ https://www.geeksforgeeks.org/a-product-array-puzzle/ """

    n = len(data)

    # Allocate memory for temporary arrays left[] and right[]
    left = [0]*n
    right = [0]*n

    # Allocate memory for the product array
    prod = [0]*n

    # Left most element of left array is always 1
    left[0] = 1

    # Rightmost most element of right array is always 1
    right[n - 1] = 1

    # Construct the left array
    for i in range(1, n):
        left[i] = data[i - 1] * left[i - 1]

    # Construct the right array
    for j in range(n-2, -1, -1):
        right[j] = data[j + 1] * right[j + 1]

    # Construct the product array using
    # left[] and right[]
    for i in range(n):
        prod[i] = left[i] * right[i]

    return prod

if __name__ == "__main__":
    expected = [120, 60, 40, 30, 24]
    assert gfg_product_of_all_numbers(data=[1, 2, 3, 4, 5]) == expected

    expected = [2, 3, 6]
    assert gfg_product_of_all_numbers(data=[3, 2, 1]) == expected
