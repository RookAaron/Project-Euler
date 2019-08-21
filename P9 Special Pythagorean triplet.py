'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
### to the power of 2 doesn't work in formatting ^^^


# these are all Pythagorean triples with hypotenous less than 100
pythagorean_triplets = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53), (11, 60, 61), (33, 56, 65), (16, 63, 65), (48, 55, 73), (36, 77, 85), (13, 84, 85), (39, 80, 89), (65, 72, 97)]


# now going to take the scalar of these
for triple in pythagorean_triplets:

    sum_of_abc = triple[0] + triple[1] + triple[2]
    
    for scalar in range(1,100):
        
        if sum_of_abc*scalar >= 1000: break

    if sum_of_abc*scalar == 1000: break

print(triple[0]*triple[1]*triple[2]*(scalar**3))
