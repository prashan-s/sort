def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left_child = 2 * i + 1  # Left child
    right_child = 2 * i + 2  # Right child

    # If left child exists and is greater than root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # If right child exists and is greater than root
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)

heap_sort(arr)
print("Sorted array:", arr)
