# Interpolation Search

- **Last Updated:** 2024-05-27
- **Programming Languages:** Python
- **Complexity:** O(log log n) (average time), O(n) (worst case time), O(1) (space)
- **Requires:** A sorted array

## Description

Interpolation Search is an algorithm for searching a key in a sorted array. It improves on the time complexity of binary search by making a more informed guess about the position of the target element, instead of always dividing the array in half. Interpolation Search calculates the probable position of the target value based on the given range and interpolates to find a closer match.

## Algorithm

The Interpolation Search algorithm works as follows:

1. Initialize low and high pointers to the start and end of the array, respectively.
2. Repeat until the search interval is not empty and the target element is within the range of the array:
    - Calculate the probe position using interpolation formula:
        ```
        probe_pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        ```
    - If the target value equals the value at the probe position, return the probe position.
    - If the target value is less than the value at the probe position, set the high pointer to probe position - 1.
    - If the target value is greater than the value at the probe position, set the low pointer to probe position + 1.
3. If the target value is not found, return -1.

