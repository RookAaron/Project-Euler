'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

number = ''
n = 0

while len(number) < 10000001:
    number += str(n)
    n += 1

total = 1
for power in range(0, 7):
    n = number[10**power]
    print(n)
    total *= int(n)
    

print(total)
