# Exponential Search

- **Last Updated:** 2024-05-29
- **Programming Languages:** Python
- **Complexity:** O(log n) (time), O(1) (space)
- **Requires:** A sorted array

## Description

Exponential Search is an algorithm used to find the position of a target value within a sorted array. It leverages binary search in a sorted subarray of size that increases exponentially to efficiently locate the range in which the target value lies.

## Algorithm

The Exponential Search algorithm works as follows:

1. Determine the range to be searched by repeatedly doubling the index `i` starting from 1 until `arr[i]` is greater than or equal to the target value or the end of the array is reached.
2. Perform binary search within the determined range for the target value.
3. If the target value is found, return its index. Otherwise, return -1.

