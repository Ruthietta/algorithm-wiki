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

def meta_binary_search(arr, target):
    n = len(arr)
    jump_size = 2  # Choose the jump size
    left = 0
    right = n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        start = max(0, mid - jump_size)
        end = min(mid + jump_size, n - 1)
        if target < arr[start]:
            right = start - 1
        elif target > arr[end]:
            left = end + 1
        else:
            return binary_search(arr, target, start, end)
    return -1

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = meta_binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
