'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

def get_length_of_recursion(n):
    n = str(n)[2:]

    prev_char = ''

    for c in n:
        if c in prev_char:
            return(len(prev_char)-prev_char.index(c))

        else:
            prev_char += c

    return(0)

largest = (1,0)
for n in range(2,1000):
    x = get_length_of_recursion(1/n)

    if x >= largest[1]:
        largest = (n,x)

print(largest)
