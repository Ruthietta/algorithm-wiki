# Fibonacci Search

- **Last Updated:** 2024-05-29
- **Programming Languages:** Python
- **Complexity:** O(log n) (time), O(1) (space)
- **Requires:** A sorted array

## Description

Fibonacci Search is an algorithm used to find the position of a target value within a sorted array. It improves on binary search by dividing the array into Fibonacci numbers instead of halves, which can reduce the number of comparisons made in certain cases.

## Algorithm

The Fibonacci Search algorithm works as follows:

1. Initialize two Fibonacci numbers `fib_m2` and `fib_m1` such that `fib_m2` is the largest Fibonacci number less than or equal to the length of the array.
2. Initialize an index `offset` to 0.
3. Repeat until the array is traversed or the target value is found:
    - Calculate the next Fibonacci number `fib` such that `fib = fib_m2 + fib_m1`.
    - If the target value is less than the value at index `offset + fib_m2`, update `fib_m2`, `fib_m1`, and `fib` accordingly.
    - If the target value is greater than the value at index `offset + fib_m2`, update `fib_m2`, `fib_m1`, `fib`, and `offset` accordingly.
    - If the target value is equal to the value at index `offset + fib_m2`, return the index `offset + fib_m2`.
4. If the target value is not found, return -1.
