#insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        
arr = list(map(int,input().split()))
insertionSort(arr)
print(arr)


#bubblesort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = list(map(int,input().split()))
bubbleSort(arr)
print(arr)



#quicksort
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
    
array = list(map(int,input().split()))
quick_sort(array, 0, len(array) - 1)
print(array)



#mergesort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
array = list(map(int,input().split()))
mergeSort(array)
print(array)


#selection sort
def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        
array = list(map(int,input().split()))
selection_sort(array)
print(array)  


#linear_search
def lin_search(a,b):
    for i in range(len(a)):
        if a[i]==b:
            return 1
        break
    return -1
a=[int(i) for i in input().split()]
b=int(input())
if (lin_search(a,b)):
    print("found at index",i)
else:
    print("not found ")
  

 
#binary search
def binarySearch(v, To_Find):
    lo = 0
    hi = len(v) - 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < To_Find:
            lo = mid + 1
        else:
            hi = mid
 
    if v[lo] == To_Find:
        print("Found At Index", lo)
    elif v[hi] == To_Find:
        print("Found At Index", hi)
    else:
        print("Not Found")
 
 
if __name__ == '__main__':
    v = [1, 3, 4, 5, 6]
    To_find = int(input())
    binarySearch(v,To_find)
