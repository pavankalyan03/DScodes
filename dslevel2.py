# Recursive Python program for insertion sort
# Recursive function to sort an array using insertion sort

def insertionSortRecursive(arr,n):
	
	if n<=1:
		return
	
	
	insertionSortRecursive(arr,n-1)
	'''Insert last element at its correct position
		in sorted array.'''
	last = arr[n-1]
	j = n-2
	
	while (j>=0 and arr[j]>last):
		arr[j+1] = arr[j]
		j = j-1

	arr[j+1]=last
	

def printArray(arr,n):
	for i in range(n):
		print(arr[i],end=" ")


arr = [12,11,13,5,6]
n = len(arr)
insertionSortRecursive(arr, n)
printArray(arr, n)


