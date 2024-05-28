def sentinel_search(arr, target):
    n = len(arr)
    last_element = arr[n - 1]
    arr[n - 1] = target

    i = 0
    while arr[i] != target:
        i += 1

    arr[n - 1] = last_element

    if i < n - 1 or arr[n - 1] == target:
        return i
    else:
        return -1

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = sentinel_search(arr, target)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
