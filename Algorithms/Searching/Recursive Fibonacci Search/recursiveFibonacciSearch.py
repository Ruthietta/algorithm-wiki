def recursive_fibonacci_search(arr, target, fib_m2, fib_m1, offset):
    if fib_m2 <= 0:
        return -1

    i = min(offset + fib_m2, len(arr) - 1)

    if arr[i] == target:
        return i
    elif arr[i] < target:
        return recursive_fibonacci_search(arr, target, fib_m1, fib_m1 - fib_m2, i)
    else:
        return recursive_fibonacci_search(arr, target, fib_m2, fib_m1 - fib_m2, offset)

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
fib_m2 = 0
fib_m1 = 1
offset = 0
result = recursive_fibonacci_search(arr, target, fib_m2, fib_m1, offset)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
