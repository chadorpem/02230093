def merge_sort(arr):
    # Edge case handling
    if arr is None:
        return None, 0, 0
    if len(arr) <= 1:
        return arr, 0, 0

    comparisons = 0
    accesses = 0

    def merge(left, right):
        nonlocal comparisons, accesses
        merged = []
        i = j = 0

        # Merge two sorted lists
        while i < len(left) and j < len(right):
            comparisons += 1
            accesses += 2  # accessing left[i] and right[j]

            if left[i] <= right[j]:
                merged.append(left[i])
                accesses += 1
                i += 1
            else:
                merged.append(right[j])
                accesses += 1
                j += 1

        # Add remaining elements
        while i < len(left):
            merged.append(left[i])
            accesses += 1
            i += 1

        while j < len(right):
            merged.append(right[j])
            accesses += 1
            j += 1

        return merged

    # Divide step
    mid = len(arr) // 2
    left, c1, a1 = merge_sort(arr[:mid])
    right, c2, a2 = merge_sort(arr[mid:])

    comparisons += c1 + c2
    accesses += a1 + a2

    # Merge step
    sorted_arr = merge(left, right)

    return sorted_arr, comparisons, accesses


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comparisons, accesses = merge_sort(arr)

print("Original List:", arr)
print("Sorted using Merge Sort:", sorted_arr)
print("Number of comparisons:", comparisons)
print("Number of array accesses:", accesses)