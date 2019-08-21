'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''


def check(n):
    if len(n) != 10: return(False)
    
    elif n.count('0') != 1: return(False)
    elif n.count('1') != 1: return(False)
    elif n.count('2') != 1: return(False)
    elif n.count('3') != 1: return(False)
    elif n.count('4') != 1: return(False)
    elif n.count('5') != 1: return(False)
    elif n.count('6') != 1: return(False)
    elif n.count('7') != 1: return(False)
    elif n.count('8') != 1: return(False)
    elif n.count('9') != 1: return(False)
    
    return(True)


numbers = ['0','1','2','3','4','5','6','7','8','9']

n_counter = 0

for n in range(123456789, 9876543210):
    if check('0'+ str(n)):
        n_counter += 1

        if n_counter == 1000000: break

print(n)
    
