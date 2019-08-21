'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def fact(n):
    if n == 0:
        return(1)
    else:
        return(n*fact(n-1))

total = 0

for n in range(10, 1000000):
    n = str(n)

    temp = 0
    for d in n:
        temp += fact(int(d))

    if temp == int(n):
        print(n)
        total += int(n)

print(total)

    
