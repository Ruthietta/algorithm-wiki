# Jump Pointer Search

- **Last Updated:** 2024-05-29
- **Programming Languages:** Python
- **Complexity:** O(n/k) (average time), O(1) (space)
- **Requires:** A sorted array

## Description

Jump Pointer Search is a variation of binary search where the search algorithm jumps to a pointer that is not the middle but a specified position, such as 1/4th or 3/4th of the array, based on the value being searched. It aims to reduce the number of comparisons in certain cases.

## Algorithm

The Jump Pointer Search algorithm works as follows:

1. Determine the jump size `k` based on the value being searched.
2. Initialize two pointers, `left` and `right`, to the start and end of the array, respectively.
3. Repeat until the search interval is empty:
    - Calculate the mid index as `left + k * (right - left)`.
    - If the target value equals the value at the mid index, return the mid index.
    - If the target value is less than the value at the mid index, set the right pointer to mid.
    - If the target value is greater than the value at the mid index, set the left pointer to mid.
4. If the target value is not found, return -1.
