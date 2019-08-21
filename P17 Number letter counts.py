'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

amount_of_letters = {
    #number: amount of letters,
    0: 0, # since you don't write it in a positive integer
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7,
    1000: 8
    }

def word_length_n(number):
    # only works for number < 10000
    wordLength = 0
    
    number = ('000'+str(number))[::-1]

    units = int(number[0])
    tens = int(number[1])
    hundreds = int(number[2])
    thousands = int(number[3])

    tens_units = int(number[1] + number[0])
    hundreds_tens_units = int(number[2] + number[1] + number[0])

    if thousands != 0:
        wordLength += amount_of_letters[1000]
        wordLength += amount_of_letters[thousands]

        if hundreds_tens_units != 0:
            wordLength += 3

    if hundreds != 0:
        wordLength += amount_of_letters[100]
        wordLength += amount_of_letters[hundreds]

        if tens_units != 0:
            wordLength += 3

    if tens_units in amount_of_letters:
        wordLength += amount_of_letters[tens_units]

    else:
        if tens != 0:
            wordLength += amount_of_letters[tens*10]

        wordLength += amount_of_letters[units]

    return(wordLength)



total_letter_count = 0

for n in range(1, 1001):
    total_letter_count += word_length_n(n)

print(total_letter_count)

    
