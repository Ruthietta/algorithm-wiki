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

def exponential_search(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, n - 1))

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = exponential_search(arr, target)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
