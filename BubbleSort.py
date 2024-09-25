lst = []
n = int(input("Enter Number of Elements: "))
for i in range(0,n):
  ele = 
  lst.append(ele) #adding the elements to the array

print(lst)
#implementation of bubblesort
def bubbleSort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(0,n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

#call to bubblesort
bubbleSort(lst)
print("Sorted array is : ")
print(lst)