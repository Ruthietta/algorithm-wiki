# Binary Search

- **Last Updated:** 2024-04-25
- **Programming Languages:** 
- **Complexity:** O(log n) (time), O(1) (space)
- **Requires:** A sorted array

## Description

Binary Search is a widely used search algorithm that finds the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half until the target value is found or the interval is empty.

## Algorithm

The Binary Search algorithm works as follows:

1. Initialize left and right pointers to the start and end of the array, respectively.
2. Repeat until the search interval is empty:
    - Calculate the mid index as the average of left and right pointers.
    - If the target value equals the value at the mid index, return the mid index.
    - If the target value is less than the value at the mid index, set the right pointer to mid - 1.
    - If the target value is greater than the value at the mid index, set the left pointer to mid + 1.
3. If the target value is not found, return -1.