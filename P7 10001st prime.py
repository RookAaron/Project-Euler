'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def isPrime(n):
    if n == 2: return(True)
    if n%2 == 0 or n < 2: return(False)
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return(False)
    return(True)

n = 1
prime_counter = 2 # needs to count 2 and 3

# all primes, except 2 and 3 are one away from a muiltiple of six

while True:
    number = 6*n

    if isPrime(number+1):
        prime_counter += 1
        if prime_counter == 10001: print(number+1)
    
    if isPrime(number-1):
        prime_counter += 1
        if prime_counter == 10001: print(number+1)

    n += 1
