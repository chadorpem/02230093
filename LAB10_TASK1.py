#Part 1: Counting Sort 
def counting_sort(arr):
    if len(arr) == 0:
        return arr
# Find maximum value
    max_val = max(arr)
# Create count array
    count = [0] * (max_val + 1)
# Count frequency
    for num in arr:
        count[num] += 1
# Build sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr
# -------- Part 2: Radix Sort --------
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0–9
# Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
        # Update count[i] to position
    for i in range(1, 10):
        count[i] += count[i - 1]
# Build output array (stable)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
# Copy to original array
    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    exp = 1
# Apply counting sort for each digit
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10

    return arr
#  Example Testing 
if __name__ == "__main__":
    arr1 = [4, 2, 2, 8, 3, 3, 1]
    print("Counting Sort Output:", counting_sort(arr1))

    arr2 = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Radix Sort Output:", radix_sort(arr2))