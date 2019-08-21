'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

def isTruncatable(n):
    n = str(n)

    rl = ''
    lr = n[:len(n)-1]

    while lr != '':
        if not isPrime(int(lr)): return False
        lr = lr[:len(lr)-1]

    for d in n[::-1]:
        rl = d + rl
        if not isPrime(int(rl)): return False

    return True

t_primes = []

n = 9
while len(t_primes) != 11:
    n += 2

    if isPrime(n):
        if isTruncatable(n):
            t_primes.append(n)

print(t_primes)
print(sum(t_primes))
