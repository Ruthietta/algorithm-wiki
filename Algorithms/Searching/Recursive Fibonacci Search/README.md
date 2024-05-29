# Recursive Fibonacci Search

- **Last Updated:** 2024-05-29
- **Programming Languages:** Python
- **Complexity:** O(log n) (time), O(log n) (space)
- **Requires:** A sorted array

## Description

Recursive Fibonacci Search is an algorithm that uses a recursive approach to search for an element in a sorted array similar to the Fibonacci sequence. It is particularly useful when the size of the array is not known in advance.

## Algorithm

The Recursive Fibonacci Search algorithm works as follows:

1. Initialize two Fibonacci numbers `fib_m2` and `fib_m1` such that `fib_m2` is the largest Fibonacci number less than or equal to the length of the array.
2. If the target value is equal to the value at index `fib_m2 - 1`, return `fib_m2 - 1`.
3. If the target value is less than the value at index `fib_m2 - 1`, recursively search within the interval `[0, fib_m2 - 2]`.
4. If the target value is greater than the value at index `fib_m2 - 1`, recursively search within the interval `[fib_m2, length of the array]`.
5. If the target value is not found, return -1.
