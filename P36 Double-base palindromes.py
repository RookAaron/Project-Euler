'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def is_palindromes(s):
    r = s[::-1]
    for i in range(len(s)):
        if r[i] != s[i]: return False
    return True

total = 0

for n_10 in range(10**6):
    n_2 = bin(n_10)[2:]

    if is_palindromes(str(n_10)) and is_palindromes(str(n_2)):
        print(n_10)
        total += n_10

print(n_10)
