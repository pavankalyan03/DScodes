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







# Python 3 program to find numbers that are product of exactly two distinct prime numbers

import math
# Function to check whether a number
# is a PerfectSquare or not
def isPerfectSquare(x):

	sr = math.sqrt(x)

	return ((sr - math.floor(sr)) == 0)

# Function to check if a number is a
# product of exactly two distinct primes
def isProduct( num):
	cnt = 0

	i = 2
	while cnt < 2 and i * i <= num:
		while (num % i == 0) :
			num //= i
			cnt += 1
		i += 1

	if (num > 1):
		cnt += 1

	return cnt == 2

# Function to find numbers that are product
# of exactly two distinct prime numbers.
def findNumbers(N):
	# Vector to store such numbers
	vec = []

	for i in range(1,N+1) :
		if (isProduct(i) and not isPerfectSquare(i)) :

			# insert in the vector
			vec.append(i)

	# Print all numbers till n from the vector
	for i in range(len( vec)):
		print(vec[i] ,end= " ")

# Driver function

	
N = int(input())
findNumbers(N)







# Recursive Python3 code to sort
# an array using selection sort
 
# Return minimum index
def minIndex( a , i , j ):
    if i == j:
        return i
         
    # Find minimum of remaining elements
    k = minIndex(a, i + 1, j)
     
    # Return minimum of current
    # and remaining.
    return (i if a[i] < a[k] else k)
     
# Recursive selection sort. n is
# size of a[] and index is index of
# starting element.
def recurSelectionSort(a, n, index = 0):
 
    # Return when starting and
    # size are same
    if index == n:
        return -1
         
    # calling minimum index function
    # for minimum index
    k = minIndex(a, index, n-1)
     
    # Swapping when index and minimum
    # index are not same
    if k != index:
        a[k], a[index] = a[index], a[k]
         
    # Recursively calling selection
    # sort function
    recurSelectionSort(a, n, index + 1)
     
# Driver code
arr = [3, 1, 5, 2, 7, 0]
n = len(arr)
 
# Calling function
recurSelectionSort(arr, n)
 
# printing sorted array
for i in arr:
    print(i, end = ' ')







# Python3 program for Recursive approach
# to find middle of singly linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data
		self.next = None
		
# Create new Node
def newLNode(data):

	temp = Node(data)
	temp.data = data
	temp.next = None
	return temp

mid = None
n = 0

# Function for finding midpoint recursively
def midpoint_util(head ):

	global n
	global mid
	
	# If we reached end of linked list
	if (head == None):
	
		n = int((n) / 2)
		return
	
	n = n + 1

	midpoint_util(head.next)

	# Rolling back, decrement n by one
	n = n - 1
	if (n == 0):
	
		# Final answer
		mid = head

def midpoint(head):

	global n
	global mid
	
	mid = None
	n = 1
	midpoint_util(head)
	return mid

# Driver Code

head = newLNode(1)
head.next = newLNode(2)
head.next.next = newLNode(3)
head.next.next.next = newLNode(4)
head.next.next.next.next = newLNode(5)
result = midpoint(head)
print( result.data )







# Python3 implementation of the approach

# Recursive function to find the sum of
# even elements from the array
def SumOfEven(arr, i, sum):

	# If current index is invalid i.e.
	# all the elements of the array
	# have been traversed
	if (i < 0):

		# Print the sum
		print(sum);
		return;

	# If current element is even
	if ((arr[i]) % 2 == 0):

		# Add it to the sum
		sum += (arr[i]);

	# Recursive call for the next element
	SumOfEven(arr, i - 1, sum);

# Driver code

arr = [ 1, 2, 3, 4, 5, 6, 7, 8 ];
n = len(arr);
sum = 0;

SumOfEven(arr, n - 1, sum);







# Recursive approach to check if an Array is sorted or not 
  
# Function that returns 0 if a pair is found unsorted 
def arraySortedOrNot(arr): 
      
    # Calculating length 
    n = len(arr) 
      
    # Array has one or no element or the 
    # rest are already checked and approved. 
    if n == 1 or n == 0: 
        return True
          
    # Recursion applied till last element 
    return arr[0]<= arr[1] and arraySortedOrNot(arr[1:]) 
  
  
arr = [20, 23, 23, 45, 78, 88] 
  
# Displaying result 
if arraySortedOrNot(arr): 
	print("Yes") 
else: 
	print("No")

	
	

	
	
	
#Print alternate nodes of a linked list using recursion	
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def alternate(self):
        self.alternate_helper(self.head)
 
    def alternate_helper(self, current):
        if current is None:
            return
        print(current.data, end = ' ')
        if current.next:
            self.alternate_helper(current.next.next)
 
a_llist = LinkedList()
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
print('The alternate nodes of the linked list: ', end = '')
a_llist.alternate()








# Python3 implementation to reverse a doubly
# linked list using recursion
import math

# a node of the doubly linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# function to get a new node
def getNode(data):
	
	# allocate space
	new_node = Node(data)
	new_node.data = data
	new_node.next = new_node.prev = None
	return new_node

# function to insert a node at the beginning
# of the Doubly Linked List
def push(head_ref, new_node):
	
	# since we are adding at the beginning,
	# prev is always None
	new_node.prev = None

	# link the old list off the new node
	new_node.next = head_ref

	# change prev of head node to new node
	if (head_ref != None):
		head_ref.prev = new_node

	# move the head to point to the new node
	head_ref = new_node
	return head_ref

# function to reverse a doubly linked list
def Reverse(node):
	
	# If empty list, return
	if not node:
		return None

	# Otherwise, swap the next and prev
	temp = node.next
	node.next = node.prev
	node.prev = temp

	# If the prev is now None, the list
	# has been fully reversed
	if not node.prev:
		return node

	# Otherwise, keep going
	return Reverse(node.prev)

# Function to print nodes in a given doubly
# linked list
def printList(head):
	while (head != None) :
		print(head.data, end = " ")
		head = head.next
	
# Driver Code
if __name__=='__main__':
	
	# Start with the empty list
	head = None

	# Create doubly linked: 10<.8<.4<.2 */
	head = push(head, getNode(2));
	head = push(head, getNode(4));
	head = push(head, getNode(8));
	head = push(head, getNode(10));
	print("Original list: ", end = "")
	printList(head)
	
	# Reverse doubly linked list
	head = Reverse(head)
	print("\nReversed list: ", end = "")
	printList(head)
	

	
	
	
	
	
	
# Python function to print permutations of a given list
def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l
 
 
# Driver program to test above function
data = list('123')
for p in permutation(data):
    print (p)








# Python Program for implementation of
# Recursive Bubble sort
class bubbleSort:
	"""
	bubbleSort:
		function:
			bubbleSortRecursive : recursive
				function to sort array
			__str__ : format print of array
			__init__ : constructor
				function in python
		variables:
			self.array = contains array
			self.length = length of array
	"""

	def __init__(self, array):
		self.array = array
		self.length = len(array)

	def __str__(self):
		return " ".join([str(x)
						for x in self.array])

	def bubbleSortRecursive(self, n=None):
		if n is None:
			n = self.length
		count = 0

		# Base case
		if n == 1:
			return
		# One pass of bubble sort. After
		# this pass, the largest element
		# is moved (or bubbled) to end.
		for i in range(n - 1):
			if self.array[i] > self.array[i + 1]:
				self.array[i], self.array[i +
				1] = self.array[i + 1], self.array[i]
				count = count + 1

		# Check if any recursion happens or not
		# If any recursion is not happen then return
		if (count==0):
			return

		# Largest element is fixed,
		# recur for remaining array
		self.bubbleSortRecursive(n - 1)

# Driver Code
def main():
	array = [64, 34, 25, 12, 22, 11, 90]
	
	# Creating object for class
	sort = bubbleSort(array)
	
	# Sorting array
	sort.bubbleSortRecursive()
	print("Sorted array :\n", sort)


if __name__ == "__main__":
	main()
	
	
	
	
'''if u learnt this all then tell me how to do also'''  


	
	
	
	



	

	
	
	
	
	

	
	



