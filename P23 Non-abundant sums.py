'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

def divisors_sum(n):
    total = 0

    for d in range(1, int(n/2)+1):
        if n%d == 0:
            total += d

    return(total)


def find_abundant_numbers():
    file = open('abundant_numbers.txt', 'w')

    for n in range(12, 28123):
        d_sum = divisors_sum(n)
        
        if d_sum > n:
            file.write(str(n))
            file.write('\n')

    file.close()


#find_abundant_numbers()

file = open('abundant_numbers.txt', 'r')

integers = []

c = 0
for line in file:
    line = line.replace('\n', '')

    integers .append(int(line))

file.close()


total = 0

for n in range(1, 28123):
    if n in integers: pass
    else:
        for i in integers:
            if n-i < 0: break

            if n-i in integers: break

            total += n

print(total)

##abundant = []
##perfect = []
##deficient = []
##
##for n in range(1, 100):
##    d_sum = divisors_sum(n)
##        
##    if d_sum > n:
##        abundant.append(n)
##
##    elif d_sum < n:
##        deficient.append(n)
##
##    else: perfect.append(n)
##
##
##for i in [abundant, perfect, deficient]:
##    for n in i:
##        print(n, divisors_sum(n))
##
##    print('\n')



            
