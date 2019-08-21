'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def fact(n):
    if n == 0: return(1)
    else: return(n*fact(n-1))

n = str(fact(100))
total = 0

for d in n:
    total += int(d)

print(total)
