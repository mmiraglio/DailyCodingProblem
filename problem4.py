# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space;
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

import numpy


def my_first_missing_positive_number(arr):
    """My solution"""
    # If the array consists only of negative numbers and zeros then
    # the first missing positive number is 1. No further calculations needed.
    # By using set we get rid of duplicates.
    positives = set(filter(lambda n: n > 0, arr))
    if len(positives) == 0:
        return 1

    positives.add(0) # For convenience 0 will always be the first element in the sorted array 
    positives =  sorted(list(positives))
    
    for i in range(len(positives)):
        if positives[i] - i > 0:
            return positives[i-1] + 1

    # If it runs until this point means that there are no missing positive numbers in the array,
    # so the result is the value of the last element in the array + 1.
    return positives[i] + 1

assert my_first_missing_positive_number([3, 4, -1, 1]) == 2
assert my_first_missing_positive_number([1, 2, 0]) == 3
assert my_first_missing_positive_number([-3, -2, -1, 0, 0, -500]) == 1
assert my_first_missing_positive_number( [1, -10, 12, 24, 2, 2, 7]) == 3
assert my_first_missing_positive_number([0]) == 1
assert my_first_missing_positive_number([1]) == 2
assert my_first_missing_positive_number([2]) == 1