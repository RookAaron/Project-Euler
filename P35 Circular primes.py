'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def isPrime(n):
    if n <= 100:
        return n in primes_under_100
    if n % 2 == 0 or n % 3 == 0:
        return False

    for f in range(5, int(n ** .5), 6):
        if n % f == 0 or n % (f + 2) == 0:
            return False
    return True

def rotate(s):
    return s[len(s)-1] + s[:len(s)-1]

c_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
total = len(c_primes)

for n in range(101, 1000000, 2):

    if n not in c_primes and isPrime(n):
        temp_primes = [n]
        temp_n = rotate(str(n))

        for _ in range(len(str(n))-1):
            if isPrime(int(temp_n)): temp_primes.append(temp_n)
            temp_n = rotate(temp_n)

        if len(temp_primes) == len(str(n)):
            for p in temp_primes:
                c_primes.append(int(p))
                total += 1

print(total)
