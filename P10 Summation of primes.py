'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def isPrime(n):
    # not going to check 2 or 3 or even numbers
    
    for i in range(5, int(n**0.5)+1, 2):
        if n%i == 0: return(False)

    return(True)


sum_of_primes = 5 # includes 2 and 3

for n in range(6, 2000000, 6):
    
    if isPrime(n-1): sum_of_primes += n-1

    if isPrime(n+1): sum_of_primes += n+1

print(sum_of_primes)
