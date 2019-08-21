'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

maxx = 1000
best = [0]*(maxx+1)

for a in range(1,maxx-1):
    for b in range(1,maxx-a):
        for c in range(1,maxx-(a+b)):
            if (a**2) + (b**2) == (c**2):
                #print(a,b,c)
                best[a+b+c] += 1


highest = [best[0], 0]

for i in range(len(best)):
    if best[i] > highest[0]:
        highest = [best[i], i]

print(highest)
                

            
