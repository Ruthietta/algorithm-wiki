def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2

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
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")
