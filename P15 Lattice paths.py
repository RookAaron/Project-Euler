'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

# 'r' = move right
# 'd' = move down

    

def move(moves, amount, size, paths):

    if len(moves) == 2*size:
        return(amount+1)

    r = moves.count('r')
    d = moves.count('d')

    if moves == '':
        amount = 2*move('r', amount, size, paths)

    else:
        if r == d:
            if size-r in paths:
                return(amount+paths[size-r])

        
        if r != size:
            amount = move(moves+'r', amount, size, paths)

        if d != size:
            amount = move(moves+'d', amount, size, paths)

    return(amount)


'''paths = {1: 2, 2: 6, 3: 20, 4: 70, 5: 252, 6: 924, 7: 3432, 8: 12870, 9: 48620, 10: 184756, 11: 705432, 12: 2704156, 13: 10400600, 14: 40116600, 15: 155117520, 16: 601080390, 17: 2333606220}

for size in range(18,19):
    amount = move('', 0, size, paths)
    paths[size] = amount
    
for i in paths:
    if i != 1:
        print(i, '\t', paths[i]/paths[i-1])'''

'''
the pattern is...

size = 3 # if grid = 3x3

times = 2 + size*4

path_length = times/size
'''


prev_amount = 2 # size = 1

for size in range (2,21):
    
    amount = int(((size*4 -2)/size)*prev_amount)

    print(size, amount)

    prev_amount = amount







