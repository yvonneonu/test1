# Python program to find out
# Sum of elements at even and
# odd index positions seperately

# Function to calculate sum
def EvenOddSum(a, n):
    even = 0
    odd = 0
    for i in range(n):

        # Loop to find even, odd Sum
        if i % 2 == 0:
            even += a[i]
        else:
            odd += a[i]

    print("Even index postions sum", even)
    print("Odd index posiions sum", odd)

# Driver Function

arr = [4, 9, 24, 30, 31, 47]
n = len(arr)

EvenOddSum(arr, n)

# This code is generated by Yvonne Onuorah

