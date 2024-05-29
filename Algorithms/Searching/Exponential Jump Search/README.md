# Exponential Jump Search

- **Last Updated:** 2024-05-29
- **Programming Languages:** Python
- **Complexity:** O(log n) (time), O(1) (space)
- **Requires:** A sorted array

## Description

Exponential Jump Search is an extension of the Jump Search algorithm where the jump size is increased exponentially instead of being constant. It can be beneficial in scenarios where the distribution of elements in the array is not uniform.

## Algorithm

The Exponential Jump Search algorithm works as follows:

1. Determine the initial jump size `k` based on the value being searched.
2. Initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
3. Repeat until the search interval is empty:
    - Calculate the mid index as `left + k`.
    - If the target value equals the value at the mid index, return the mid index.
    - If the target value is less than the value at the mid index, set the right pointer to mid.
    - If the target value is greater than the value at the mid index, set the left pointer to mid.
    - Update the jump size `k` to `2 * k`.
4. If the target value is not found, return -1.
