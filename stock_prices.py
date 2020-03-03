import operator


def my_get_max_profit(stock_prices):
    """ 
    Given a list of stock prices returns the maximum profit that could have been obtained by an investor 
    buying a single stock at the lowest price and selling at the max price.
    """
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # Sorts the list of Stock Prices keeping the original indexes. It's important to keep
    # this information because it represents the time of the day that the stock reachead that price.
    # For the input suggested in the problem:
    #
    # stock_prices = [10, 7, 5, 8, 11, 9]
    # will result in:
    # stock_prices_ordered = [(4, 11), (0, 10), (5, 9), (3, 8), (1, 7), (2, 5)]
    # where the first element of the tuple represent the index (time) and the second the stock price.
    stock_prices_sorted = sorted(
        enumerate(stock_prices), key=operator.itemgetter(1), reverse=True)

    # Traverse the ordered list of stock prices in order to find the maximum difference
    # between the element being evaluated and the rest of the list.
    # For the example input list, the first iteration will take the Max value
    # Max = (4, $11) => max_i = 4 and max_value = 11
    # and will compare it against the other elements, starting for the last element which represents
    # the lowest price reached by the stock on that day.
    # [(0, 10), (5, 9), (3, 8), (1, 7), (2, 5)]
    # Min = (2, $5)
    # max_value - min_value = 11 - 5 = 6, a nice spread, but we need check the order
    # that those events ocurred in time; By doing that (comparing indexes) we find out
    # that the Price $5 was reached BEFORE $11 (making it possible buying for $5 and selling for $11),
    # so that is our partial answer. To have the definitive one is necessary to have the rest of the max spreads possible.
    # So we move to the next Max in the list (0, 10) and compare it against the rest of the elements
    # [(5, 9), (3, 8), (1, 7), (2, 5)] (starting again for the last element, the lowest price of the day)
    l = len(stock_prices_sorted)
    partials = [None] * l  # Array to maintain our partial anwsers
    for i in range(l - 1):
        max_i, max_value = stock_prices_sorted[i]
        for y in range(l - 1,  i, -1):
            min_i, min_value = stock_prices_sorted[y]
            if max_i > min_i:
                partials[i] = max_value - min_value
                break

    # We are not interested in None values
    partials = [n for n in partials if n is not None]

    # If the algorithm was able to find a suitable moment
    # to sell the stock the spread will be in the list of
    # partials, if not just try to minimze the losses (for the
    # case prices just went down during the day)
    if partials:
        return max(partials)
    else:
        return stock_prices_sorted[1][1] - stock_prices_sorted[0][1]


def ic_get_max_profit(stock_prices):
    """ 
    This one's a good example of the greedy ↴ approach in action. 
    Greedy approaches are great because they're fast (usually just one pass through the input). 
    """
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit


if __name__ == "__main__":
    stock_prices = [10, 7, 5, 8, 11, 9]
    # Returns 6 (buying for $5 and selling for $11)
    assert my_get_max_profit(stock_prices) == 6
    assert ic_get_max_profit(stock_prices) == 6

    stock_prices = [10, 10, 10]
    # Returns 0 because the stock price didn't changed during the day
    assert my_get_max_profit(stock_prices) == 0
    assert ic_get_max_profit(stock_prices) == 0

    stock_prices = [10, 5, 10, 5, 10, 5]
    # Returns 5 (buying for $5 and selling for $10)
    assert my_get_max_profit(stock_prices) == 5
    assert ic_get_max_profit(stock_prices) == 5

    stock_prices = [25, 30, 12, 20, 5, 12]
    # Returns 8 (buying for $12 and selling for $20)
    assert my_get_max_profit(stock_prices) == 8
    assert ic_get_max_profit(stock_prices) == 8

    stock_prices = [50, 45, 40, 30, 20, 10]
    # Stocks just went down, so the best it can be done is
    # minimize the losses :(
    assert my_get_max_profit(stock_prices) == -5
    assert ic_get_max_profit(stock_prices) == -5
