import random

arr = []

n = int(input("How many time : "))

for i in range(0,n):
    x=random.randint(1,10000)
    arr.append(x)
print(arr)

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1


def quickSort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

quickSort(arr,0,n-1)
print(arr)
