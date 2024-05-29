import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    return -1

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = jump_search(arr, target)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
