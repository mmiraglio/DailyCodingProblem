# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

k = 17
data = [10, 15, 3, 7]


def add_up_to_number(data, k):

    for n1 in data:
        for n2 in data:
            if n1 + n2 == k:
                print(
                    "Found two numbers that add up to {}; ({} and {}).".format(k, n1, n2))
                return True

    return False


print(add_up_to_number(data, k))