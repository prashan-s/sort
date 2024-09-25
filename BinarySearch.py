from pygorithm.sorting import bubble_sort

def binary_search(arr, min, max, key):
    if max < min:
        return False
    else:
        mid = (min + max) // 2
        if arr[mid] > key:
            return binary_search(arr, min, mid - 1, key)
        elif arr[mid] < key:
            return binary_search(arr, mid + 1, max, key)
        else:
            return mid

# Function to read sorted numbers from the user and store them in an array
def read_sorted_numbers():
    n = int(input("Enter the number of elements: "))
    arr = []
    print("Enter the sorted numbers:")
    for _ in range(n):
        num = int(input())
        arr.append(num)
    return arr

# Example usage
arr = read_sorted_numbers()
key = int(input("Enter the number to search: "))
result = binary_search(arr, 0, len(arr) - 1, key)

if result is False:
    print("Number not found in the array")
else:
    print("Number found at index:", result)
