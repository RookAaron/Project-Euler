'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from itertools import permutations

numbers = []
total = []

for new in range(1,10):
    numbers.append(new)

for n in permutations(numbers):
    n1 = ''
    for first in range(0, len(numbers)-2):
        n1 += str(n[first])
        n2 = ''
        for second in range(first+1, len(numbers)-1):
            n2 += str(n[second])
            n3 = ''
            if int(n2) > int(n1): break
            
            for third in range(second+1, len(numbers)):
                n3 += str(n[third])

            if eval(n1+'*'+n2) == eval(n3):
                if int(n3) not in total: total.append(int(n3))

print(sum(total))
                
