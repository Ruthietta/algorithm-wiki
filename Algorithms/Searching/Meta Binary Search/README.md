# Meta Binary Search

- **Last Updated:** 2024-05-29
- **Programming Languages:** Python
- **Complexity:** O(log(log n)) (time), O(1) (space)
- **Requires:** A sorted array

## Description

Meta Binary Search is an algorithm used to find an element in a sorted array. It is a variation of the binary search algorithm that optimizes for the number of comparisons made in each iteration, aiming to reduce the logarithmic factor of the standard binary search.

## Algorithm

The Meta Binary Search algorithm works as follows:

1. Choose a jump size `k`, typically a constant (e.g., 2).
2. Initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
3. Repeat until the search interval is small enough:
    - Calculate the mid index as `left + (right - left) // 2`.
    - Perform a binary search within the interval `[mid - k, mid + k]`.
    - If the target value is found, return its index.
    - If the target value is less than the value at the mid index, set `right` to `mid - 1`.
    - If the target value is greater than the value at the mid index, set `left` to `mid + 1`.
4. If the target value is not found, return -1.
