def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high and arr[low] <= target <= arr[high]:
        probe_pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[probe_pos] == target:
            return probe_pos
        elif arr[probe_pos] > target:
            high = probe_pos - 1
        else:
            low = probe_pos + 1
    return -1

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 7
result = interpolation_search(my_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the list.")
