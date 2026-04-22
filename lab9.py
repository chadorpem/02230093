#task 1
def selection_sort(arr):
    n = len(arr)
    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i  # assume current position is minimum

        # find the index of the smallest element in remaining list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # print list after each pass
        print(f"Pass {i + 1}: {arr}")

    print("Sorted list:", arr)
# Sample Input
arr = [29, 10, 14, 37, 13]
selection_sort(arr)

#task 2
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    print("Original list:", arr)

    for i in range(n - 1):
        min_index = i

        # find the smallest element in remaining list
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j

        # swap if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

        print(f"Pass {i + 1}: {arr}")

    print("Sorted list:", arr)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)


# same main code (no change needed)
arr = [29, 10, 14, 37, 13]
selection_sort(arr)
#task 3
def create_index_table(arr, block_size):
    index_table = []

    # go through the array in steps of block_size
    for i in range(0, len(arr), block_size):
        # store (value, index)
        index_table.append((arr[i], i))

    return index_table


# Example usage (after sorting)
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
block_size = 3

index_table = create_index_table(arr, block_size)

print("Index Table:")
for value, index in index_table:
    print(f"Value: {value}, Index: {index}")

#task 4
def indexed_search(arr,index_table,key):
    print("Search key:",key)
    n=len(index_table)
    for i in range(n):
        if i==n-1 or key<index_table[i+1][0]:
            imin=index_table[i][1]
            if i==n-1:
                imax=len(arr)-1
                print("Index range found:")
                print(f"{index_table[i][0]} <= {key}")
            else:
                imax=index_table[i+1][1]-1
                print("Index range found:")
                print(f"{index_table[i][0]} <= {key} < {index_table[i+1][0]}")
            break
    print(f"Searching from index {imin} to index {imax}:")
    for j in range(imin,imax+1):
        print(j)
        print(f"Checking index {j}: {arr[j]}")
        if arr[j]==key:
            print(f"{key} found at index {j}")
            return j
    print("Element not found")
    return -1

arr=[10,15,20,25,30,35,40,45,50,55,60,65]
index_table=[(10,0),(25,3),(40,6),(55,9)]
key=45
indexed_search(arr,index_table,key)
#task 5
def indexed_search(arr,index_table,key):
    print("Search key:",key)
    n=len(index_table)
    for i in range(n):
        if i==n-1 or key<index_table[i+1][0]:
            imin=index_table[i][1]
            if i==n-1:
                imax=len(arr)-1
                print("Index range found:")
                print(f"{index_table[i][0]} <= {key}")
            else:
                imax=index_table[i+1][1]-1
                print("Index range found:")
                print(f"{index_table[i][0]} <= {key} < {index_table[i+1][0]}")
            break
    print(f"Searching from index {imin} to index {imax}:")
    for j in range(imin,imax+1):
        print(f"Checking index {j}: {arr[j]}")
        if arr[j]==key:
            print(f"{key} found at index {j}")
            return j
    print(f"{key} not found")
    return -1

arr=[10,15,20,25,30,35,40,45,50,55,60,65]
index_table=[(10,0),(25,3),(40,6),(55,9)]
key=43
indexed_search(arr,index_table,key)