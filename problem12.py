from itertools import product


def climb_staircase(x, n):
    """
    There exists a staircase with N steps, you can climb any number from a set of positive integers X.
    Returns the number of unique ways you can climb the staircase.     

    For example, if N is 4, then there are 5 unique ways:
        1, 1, 1, 1
        2, 1, 1
        1, 2, 1
        1, 1, 2
        2, 2
    """

    # It doesn't make sense steps greater than N nor duplicated values
    x2 = [(el,) for el in set(x) if el <= n]

    if not x2:
        return []

    result = []
    while x2:
        discard = []
        for step in x2:
            s = sum(step)
            if s == n:  # Check if the tuple is a valid combination of steps
                result.append(step)
            elif s > n:
                # Check if the tuple should be discarded on next iterations
                # because it already has a larger number of steps than N
                discard.append(step)

        if discard:
            x2 = set(x2) - set(discard)

        x2 = [(*el[0], el[1]) for el in product(x2, x)]

    return result


if __name__ == "__main__":

    print("-" * 100)
    print("Possible combinations for X=[1,2] and N=4")
    print(climb_staircase([1, 2], 4))
    print()

    print("-" * 100)
    print("Possible combinations for X=[1, 3, 5] and N=5")
    print(climb_staircase([1, 3, 5], 5))
    print()

    print("-" * 100)
    print("Possible combinations for X=[1, 3, 5] and N=4")
    print(climb_staircase([1, 3, 5], 4))
    print()

    print("-" * 100)
    print("Possible combinations for X=[3, 5, 7] and N=4")
    print(climb_staircase([3, 5, 7], 4))
    print()

    print("-" * 100)
    print("Possible combinations for X=[3, 5, 7, 9, 13, 14, 15, 20, 22, 30] and N=60")
    print(climb_staircase([14, 15, 20, 22, 30], 60))
    print()