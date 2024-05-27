# Ternary Search
- **Last Updated:** 2024-05-23
- **Programming Languages:** Python
- **Complexity:** O(log3 n) (time), O(1) (space)
- **Requires:** A sorted array

## Description

Ternary Search is a divide-and-conquer algorithm used for searching in ordered lists or arrays. It is similar to binary search, but instead of dividing the array into two parts, ternary search divides it into three parts and determines which part the target element lies in. This process continues until the target element is found or the search interval is empty.

## Algorithm

The Ternary Search algorithm works as follows:

1. Initialize left and right pointers to the start and end of the array, respectively.
2. Repeat until the search interval is empty:
    - Calculate two midpoints, mid1 and mid2, dividing the search interval into three equal parts.
    - If the target value equals the value at mid1 or mid2, return the index of the midpoint where the target is found.
    - If the target value is less than the value at mid1, search in the left third of the array.
    - If the target value is greater than the value at mid2, search in the right third of the array.
    - If the target value is between mid1 and mid2, search in the middle third of the array.
3. If the target value is not found, return -1.

