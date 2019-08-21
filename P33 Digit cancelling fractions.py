'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

for n in range(10,100):
    for d in range(n+1, 100):
        n = str(n)
        d = str(d)

        if '0' in list(n) or '0' in list(d): continue

        for i in range(0,2):
            for j in range(0,2):
                if n[i] == d[j]:
                    if int(n)/int(d) == int(n[i-1])/int(d[j-1]):
                        print(n,d)
