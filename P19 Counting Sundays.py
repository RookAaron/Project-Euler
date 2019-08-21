'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


months = {
    # month as number: amount of days,
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }


sundays_on_1st = 0

day = 2 #day -> 1 = mon, tue = 2 ... sun = 7

'''
start = 1 jan 1901 (tue)
end = 31 dec 2000
'''

for year in range(1901, 2001):
    for month in range(1, 13):

        days_in_month = months[month]

        if month == 2:
            # check if leap year
            if year%100 == 0: # centry
                if year%400 == 0:
                    days_in_month += 1
            elif year%4 == 0:
                days_in_month += 1


        day += days_in_month%7

        while day > 7: day -= 7

        if day == 7:
            sundays_on_1st += 1


print(sundays_on_1st)
        
