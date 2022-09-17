#product of 2 numbers.
def product( x , y ):
    if x < y:
        return product(y, x)
    elif y != 0:
        return (x + product(x, y - 1))
    else:
        return 0 
x=int(input())
y=int(input())
print( product(x, y))




# Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)
num = int(input())

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
	 
	 


# Function to find factorial of given number
def factorial(n):
      
    if n == 0:
        return 1
     
    return n * factorial(n-1)
  
# Driver Code
num = int(input())
print("Factorial of", num, "is",
factorial(num)) 




#nth term of febonacci.
def solve(n):
   if n <= 2:
      return n - 1
   else:
      return solve(n - 1) + solve(n - 2)

n = 8
print(solve(n))



#power of 2numbers
def power(N, P):
    if P == 0:  # base condition
        return 1
    return (N*power(N, P-1)) 
 
# Driver program
N=int(input())
P=int(input())
 
print(power(N, P))



#prime number
def Prime_Number(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    return Prime_Number(n, i + 1)


n = int(input())
if Prime_Number(n):
    print("Yes,", n, "is Prime")
else:
    print("No,", n, "is not a Prime")
		
		
		
		
		
# Python implementation to add numbers without any arthemetic operators
def add(a, b):
    
    for i in range(1, b + 1):
        a = a + 1
    return a
a = add(10, 32)
print(a)




# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = int(input())

convertToBinary(dec)
print()




# Python3 program to find all the factors
def factors(n, i):
    if (i <= n):
        if (n % i == 0):
            print(i, end = " ");
        factors(n, i + 1);
     
# Driver code
N =int(input())
factors(N, 1)



#max product sum
def maxProd(N):
 
    if (N == 0):
        return 1
    if (N < 10):
        return N
    return max(maxProd(N // 10) * (N % 10),
               maxProd(N // 10 - 1) * 9)
 

N = int(input())
print(maxProd(N))
		
		
		
		
