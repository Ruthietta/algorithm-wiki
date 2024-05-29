def fibonacci_search(arr, target):
    fib_m2 = 0
    fib_m1 = 1
    fib = fib_m1 + fib_m2
    n = len(arr)

    while fib < n:
        fib_m2 = fib_m1
        fib_m1 = fib
        fib = fib_m1 + fib_m2

    offset = 0
    while fib > 1:
        i = min(offset + fib_m2, n - 1)
        if arr[i] < target:
            fib = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib - fib_m1
            offset = i
        elif arr[i] > target:
            fib = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib - fib_m1
        else:
            return i

    if fib_m1 == 1 and arr[offset] == target:
        return offset

    return -1

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = fibonacci_search(arr, target)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
