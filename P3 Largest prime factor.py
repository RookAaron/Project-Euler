'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

def isPrime(n):
    for i in range(2, int(n/2)+1):
        if n%i == 0: return(False)
    return(True)

factors = [71, 839, 1471]

for j in range(1472, 600851475143):
    if 600851475143%j == 0: break

print(j)
               
for i in range(int(298868831317/j), 3, -1):
    if 600851475143%i == 0 and isPrime(i): break

print(i)
