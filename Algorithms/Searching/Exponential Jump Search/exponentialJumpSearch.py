def binary_search(arr, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_jump_search(arr, target):
    n = len(arr)
    jump_size = 1
    while jump_size < n and arr[jump_size] < target:
        jump_size *= 2
    left = jump_size // 2
    right = min(jump_size, n - 1)
    return binary_search(arr, target, left, right)

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = exponential_jump_search(arr, target)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
