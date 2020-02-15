# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


def add_up_to_number(data, k):

    for n1 in data:
        for n2 in data:
            if n1 + n2 == k:
                print(
                    "Found two numbers that add up to {}; ({} and {}).".format(k, n1, n2))
                return True

    return False


print(add_up_to_number(data=[10, 15, 3, 7], k=17))
print(add_up_to_number(data=[0, 15, 3, 0], k=0))
print(add_up_to_number(data=[1, 100, -10, 7, 10], k=0))
print(add_up_to_number(data=[1, 100, -5, 7, 10, 94], k=95))
print(add_up_to_number(data=[100, 94, -5, 7, 10, 1], k=95))

print(add_up_to_number(data=[100, 94, -5, 7, 10, 1], k=1000))