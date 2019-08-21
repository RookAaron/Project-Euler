'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
# REQUIRES TEXT FILE

from time import perf_counter as stopwatch

file = open('names_for_P22.txt', 'r')

names = []
name = ''

for char in file.read():
    if char == '"': pass
    elif char == ',':
        names.append(name)
        name = ''
    else: name += char
names.append(name)            

file.close()

start = stopwatch()

def compare_alphebetically(name1, name2):
    ''' returns 1 if name1 < name2
returns 0 otherwise '''

    if name1 in name2:
        if name2[:len(name1)] == name1:
            return(0)
    if name2 in name1:
        if name1[:len(name2)] == name2:
            return(1)


    for i in range(0, len(name1)):
        if ord(name1[i]) < ord(name2[i]): return(0)
        if ord(name1[i]) > ord(name2[i]): return(1)
         

def sort(names):

    if names == []: return([])

    above = []
    below = []

    name = names[0]
    names.remove(name)

    for n in names:
        if compare_alphebetically(name, n) == 0:
            below.append(n)
        else:
            above.append(n)


    return(sort(above) + [name] + sort(below))


names = sort(names)

total_score = 0
counter = 1

for name in names:
    name_score = 0

    for char in name:
        name_score += ord(char)-(ord('A')-1)

    total_score += name_score * counter

    counter += 1

end = stopwatch()

print(total_score)
print(end-start)
