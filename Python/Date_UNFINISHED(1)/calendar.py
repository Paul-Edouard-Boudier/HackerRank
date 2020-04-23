from datetime import date

date_l = [int(x) for x in input().split()]
print(date(date_l[2], date_l[0], date_l[1]).strftime('%A').upper())

# OR :

import calendar

d = [int(x) for x in input().split()]
print(calendar.day_name[calendar.weekday(d[2], d[0], d[1])].upper())