'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(n):
    n = str(n)
    n_backwards = ''
    for i in n: n_backwards = i + n_backwards

    if n == n_backwards: return(True)
    return(False)

# i am going to assume both numbers are greater than 800

largest = 0

for n1 in range(999, 99, -1):
    for n2 in range(n1, 99, -1):
        if isPalindrome(n1*n2):
            if n1*n2 > largest: largest = n1*n2

print(largest)
