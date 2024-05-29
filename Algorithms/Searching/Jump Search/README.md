# Jump Search

- **Last Updated:** 2024-05-29
- **Programming Languages:** Python
- **Complexity:** O(√n) (time), O(1) (space)
- **Requires:** A sorted array

## Description

Jump Search is an algorithm used to find the position of a target value within a sorted array. It works by jumping ahead by fixed steps to cover larger portions of the array, and then performing linear search in the smaller intervals to find the target value.

## Algorithm

The Jump Search algorithm works as follows:

1. Determine the block size `m`. Typically, `m` is chosen as the square root of the array length `n`.
2. Jump ahead by `m` steps in the array until an element greater than or equal to the target value is found or the end of the array is reached.
3. Perform a linear search in the block starting from the previous block's index and ending at the current index.
4. If the target value is found, return its index. Otherwise, continue jumping and searching until the target value is found or the end of the array is reached.
5. If the target value is not found, return -1.

