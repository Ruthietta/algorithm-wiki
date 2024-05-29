# Sentinel Search

- **Last Updated:** 2024-05-28
- **Programming Languages:** Python
- **Complexity:** O(n) (time), O(1) (space)
- **Requires:** A sorted array

## Description

Sentinel Search, also known as Linear Search with Sentinel, is a variation of the linear search algorithm. It improves the linear search by reducing the number of comparisons made inside the loop. 

## Algorithm

The Sentinel Search algorithm works as follows:

1. Append the target value to the end of the array.
2. Set a sentinel value as the target value at the end of the array.
3. Start iterating through the array from the beginning:
    - Compare each element with the target value.
    - If the target value is found at the current index, return the index.
4. If the target value is not found after iterating through the array, return -1.
