def quick_sort(arr):
    # Edge case
    if arr is None or len(arr) <= 1:
        return arr, 0, 0

    comparisons = 0
    swaps = 0

    def median_of_three(a, low, high):
        nonlocal comparisons, swaps
        mid = (low + high) // 2

        # ترتيب العناصر الثلاثة: low, mid, high
        if a[low] > a[mid]:
            a[low], a[mid] = a[mid], a[low]
            swaps += 1
        comparisons += 1

        if a[low] > a[high]:
            a[low], a[high] = a[high], a[low]
            swaps += 1
        comparisons += 1

        if a[mid] > a[high]:
            a[mid], a[high] = a[high], a[mid]
            swaps += 1
        comparisons += 1

        # Use middle element as pivot (after ordering)
        a[mid], a[high - 1] = a[high - 1], a[mid]
        swaps += 1
        return a[high - 1]

    def partition(a, low, high):
        nonlocal comparisons, swaps

        pivot = median_of_three(a, low, high)
        i = low
        j = high - 1

        while True:
            i += 1
            while a[i] < pivot:
                comparisons += 1
                i += 1
            comparisons += 1

            j -= 1
            while a[j] > pivot:
                comparisons += 1
                j -= 1
            comparisons += 1

            if i >= j:
                break

            a[i], a[j] = a[j], a[i]
            swaps += 1

        # Place pivot in correct position
        a[i], a[high - 1] = a[high - 1], a[i]
        swaps += 1
        return i

    def quicksort_recursive(a, low, high):
        if low < high:
            if high - low + 1 >= 3:
                pivot_index = partition(a, low, high)
                quicksort_recursive(a, low, pivot_index - 1)
                quicksort_recursive(a, pivot_index + 1, high)
            else:
                # Simple sort for small arrays
                if a[low] > a[high]:
                    a[low], a[high] = a[high], a[low]

    quicksort_recursive(arr, 0, len(arr) - 1)
    return arr, comparisons, swaps


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comparisons, swaps = quick_sort(arr.copy())

print("Original List:", arr)
print("Sorted using Quick Sort:", sorted_arr)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)