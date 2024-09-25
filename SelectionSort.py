arr = []

n = int(input("How many time : "))

for i in range(0,n):
    x=int(input("Enter Number : "))
    arr.append(x)

print(arr)

def selectionSort(A):
    n=len(A)
    for j in range(0,n-1):
        smallest = j
        for i in range(j+1,n):
            if A[i]<A[smallest]:
                smallest = i
        A[j],A[smallest] = A[smallest],A[j]

selectionSort(arr)
print(arr)
