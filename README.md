# Solutions to problems sent by Daily Coding Problem site. #

## Problem 1: ##
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given `[10, 15, 3, 7]` and k of 17, return true since 10 + 7 is 17.

_Bonus: Can you do this in one pass?_

## Problem 2: ##
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be [2, 3, 6].

_Follow-up: what if you can't use division?_

## Problem 3: ##
This problem was asked by Google.

Given the root to a binary tree, implement `serialize(root)`, which serializes the tree into a string, and `deserialize(s)`, which deserializes the string back into the tree.

For example, given the following Node class
```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:
```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

## Problem 4: ##
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.

## Problem 5: ##
This problem was asked by Jane Street.

``cons(a, b)`` constructs a pair, and ``car(pair)`` and ``cdr(pair)`` returns the first and last element of that pair. For example, ``car(cons(3, 4))`` returns ``3``, and ``cdr(cons(3, 4))`` returns ``4``.

Given this implementation of cons:
```
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement ``car`` and ``cdr``.

## Problem 6: ##
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to ``get_pointer`` and ``dereference_pointer`` functions that converts between nodes and memory addresses.

## Problem 10: ##
This problem was asked by Apple.
Implement a job scheduler which takes in a function ``f`` and an integer ``n``, and calls ``f`` after ``n`` milliseconds.

## Problem 12: ##
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if ``X = {1, 3, 5}``, you could climb 1, 3, or 5 steps at a time.