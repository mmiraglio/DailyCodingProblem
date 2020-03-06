class Log:
    """ Data structure to record the last N order ids in a log. """

    def __init__(self):
        self.data = []

    def record(self, order_id):
        """ Adds the order_id to the log """
        self.data.append(order_id)

    def get_last(self, i):
        """
        Gets the ith last element from the log. 
        i is guaranteed to be smaller than or equal to N. 
        """
        return self.data[len(self.data) - 1 - i]


if __name__ == "__main__":

    log = Log()
    for order_num in range(100, 120):
        log.record(order_num)

    assert log.get_last(0) == 119
    assert log.get_last(1) == 118
