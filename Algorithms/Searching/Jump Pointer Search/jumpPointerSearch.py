def jump_pointer_search(arr, target):
    n = len(arr)
    jump_size = 2  # Choose the jump size
    left = 0
    right = n - 1
    while left <= right:
        mid = left + jump_size * (right - left)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = jump_pointer_search(arr, target)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
