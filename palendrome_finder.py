from datetime import datetime
from datetime import timedelta
from datetime import date

count = 0

def find_palindromes(start_date, day_count):
    for i in xrange(0,day_count):
        if start_date.month in range (1,10):
            month = '0' + str(start_date.month)
        else:
            month = str(start_date.month)

        if start_date.day in range(1,10):
            day = '0' + str(start_date.day)
        else:
            day = str(start_date.day)

        monthDay = month + day
        if monthDay == str(start_date.year)[::-1]:
            global count
            count += 1
            print "Palindrome Found: {}{}".format(monthDay, str(start_date.year))
        start_date += timedelta(days=1)

    print "Total number of Palindromes found: {}".format(count)

def find_century(year):
    if (year % 100) >= 50:
        century_start = int(round(year, -2)) - 100
        century_end = int(round(year, -2))
    else:
        century_start = int(round(year, -2))
        century_end = int(round(year, -2)) + 100

    print 'Searching for palindromes between the years {} and {}\n'.format(century_start, century_end)
    start_date = datetime.now().date().replace(year=century_start, month=1, day=1)    
    end_date = datetime.now().date().replace(year=century_end-1, month=12, day=31)
    day_count = (end_date - start_date).days # Tracks the total amount of days in a given century
    find_palindromes(start_date, day_count)

# Only works with dates between 1000-9999
# Can easily use exception handling to filter out invalid inputs
year = raw_input("Enter a year between 1000 A.D. and 9999 A.D.")
find_century(int(year))
