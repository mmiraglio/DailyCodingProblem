# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6]

import numpy

def my_product_of_all_numbers(data):
    """My solution."""
    mult = numpy.prod(data)
    result = [None] * len(data) 
    for i, value in enumerate(data):
        result[i] = mult / value

    return result

expected = [120, 60, 40, 30, 24]
assert my_product_of_all_numbers(data=[1, 2, 3, 4, 5]) == expected

expected = [2, 3, 6]
assert my_product_of_all_numbers(data=[3,2,1]) == expected
