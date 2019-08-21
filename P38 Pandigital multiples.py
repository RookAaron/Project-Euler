'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def isPandigital(s):
    if '0' in s: return False
    for n in range(1,10):
        if s.count(str(n)) != 1: return False
    return True

largest = 0
multiples = [1]

for m in range(2,50):
    multiples.append(m)

    n = 1
    cm = ''
    while len(cm) <= 9:
        cm = ''
        for i in multiples:
            cm += str(n*i)
            
        if isPandigital(cm):
            print(n, multiples, cm)
            if int(cm) > largest:
                largest = int(cm)

        n += 1

print(largest)
