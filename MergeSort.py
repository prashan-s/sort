def merge_sort(arr, l, r):
    if l < r:
        q = (l + r) // 2
        merge_sort(arr, l, q)
        merge_sort(arr, q + 1, r)
        merge(arr, l, q, r)

def merge(arr, l, q, r):
    n1 = q - l + 1
    n2 = r - q

    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[q + 1 + j]

    # Merge the temporary arrays back into arr[l..r]
    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
merge_sort(arr, 0, n - 1)
print("Sorted array:", arr)
