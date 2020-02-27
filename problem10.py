# This problem was asked by Apple.
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import datetime as dt
# >>> a = datetime.datetime.now()
# >>> b = datetime.datetime.now()
# >>> c = b - a
# int(delta.total_seconds() * 1000) # milliseconds


def set_interval(f, n):
    # Perform some basic validations
    if f is None:
        raise Exception("parameter f cannot be None")
    if n < 1:
        raise Exception("param n cannot be less than 1.")

    last_execution = dt.datetime.now()
    while True:
        elapsed_milliseconds = int(
            (dt.datetime.now() - last_execution).total_seconds() * 1000)

        if elapsed_milliseconds >= n:
            f()
            last_execution = dt.datetime.now()


def custom_func():
    print("I was executed!")


set_interval(custom_func, 2500)
