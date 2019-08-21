'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

n = 2520

while True:
    n += 2520 # adding this because anything smaller won't be divisable by numbers between 1 and 10

    correct_n = True
    for divisors in range(2, 21):
        if n%divisors != 0:
            correct_n = False
            break

    if correct_n == True: break

print(n)
