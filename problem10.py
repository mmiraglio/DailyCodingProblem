# This problem was asked by Apple.
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import datetime as dt
import threading


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


def custom_func2():
    print("Yay... I was also executed!")


if __name__ == "__main__":
    # Threads are set to daemon so are automatically terminated when all non-daemon threads (including main) exit.
    # Thread 1
    threading.Thread(target=set_interval, args=(
        custom_func, 500), daemon=True).start()
    # Thread 2
    threading.Thread(target=set_interval, args=(
        custom_func2, 1000), daemon=True).start()
    while True:
        if input('Press (q)uit to exit the program)') == "q":
            break
