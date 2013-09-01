# coding=utf-8
import datetime
import timeit
import pytz

__author__ = 'Giyyan'


def count_day(start_date, wdays, days={0, 1, 2, 3, 4}):
    week_range = (range(7) * (wdays / 5 + 1))[start_date.weekday():]
    count = 0
    for indx, item in enumerate(week_range):
        if item in days:
            count += 1
        if count == wdays:
            week_range = week_range[:indx + 1]
            break
    return week_range


def get_last_day(start_date, wdays):
    """
    Дату последнего дня после wdays будних дней
    """
    f_week = wdays / 5 + 1
    first_day = start_date.weekday()

    if abs(wdays + first_day) > 5 and f_week == 1:
        f_week = 2

    week_range = (range(7) * f_week)[first_day:]
    weenends = (7 - 5) * (f_week - 1)
    if first_day > 4:
        weenends -= 7 - first_day
    last_day = len(week_range[first_day:]) - wdays - weenends
    return start_date + datetime.timedelta(days=len(week_range[first_day:-last_day]))


def work_day_count(start_date, work_days, need_days={0, 1, 2, 3, 4}):
    n = 0
    while n < work_days:
        if start_date.weekday() in need_days:
            n += 1
        start_date += datetime.timedelta(days=1)
    return start_date


def _dedline_start(date, days):
        start_line = datetime.datetime.now(pytz.utc)
        if days and days > 0:
            start_date = datetime.datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=pytz.utc)
            start_line = start_date
            count = 0
            while count < days:
                if datetime.datetime.weekday(start_line + datetime.timedelta(days=1)) == 5:
                    start_line = start_line + datetime.timedelta(days=3)
                elif datetime.datetime.weekday(start_line + datetime.timedelta(days=1)) == 6:
                    start_line = start_line + datetime.timedelta(days=2)
                else:
                    start_line = start_line + datetime.timedelta(days=1)
                count += 1
        return start_line


print get_last_day(datetime.date(2013, 9, 2), 3)


#print work_day_count(datetime.date(2013, 8, 1), 3)
#print timeit.timeit('work_day_count(datetime.date(2013, 8, 1), 10000)', "from __main__ import work_day_count; import datetime", number=1)
#print datetime.date(2013, 8, 1) + datetime.timedelta(days=len(count_day(datetime.date(2013, 8, 1), 3)))
#print timeit.timeit('datetime.date(2013, 8, 1) + datetime.timedelta(days=len(count_day(datetime.date(2013, 8, 1), 10000)))', "from __main__ import count_day; import datetime", number=1)
#print _dedline_start('2013-08-01', 3)
#print timeit.timeit('_dedline_start("2013-08-01", 10000)', "from __main__ import _dedline_start; import datetime; import pytz", number=1)
#print get_last_day(datetime.date(2013, 8, 1), 3)
#print timeit.timeit('datetime.date(2013, 8, 1) + datetime.timedelta(days=len(count_selected_day(datetime.date(2013, 8, 1), 10000)))', "from __main__ import count_selected_day; import datetime", number=1)
#print get_last_day(datetime.date(2013, 8, 1), 3)
#print timeit.timeit('datetime.date(2013, 8, 1) + datetime.timedelta(days=len(count_selected_day(datetime.date(2013, 8, 1), 10)))', "from __main__ import count_selected_day; import datetime", number=1)
#print timeit.timeit('datetime.date(2013, 8, 1) + datetime.timedelta(days=len(count_selected_day(datetime.date(2013, 8, 1), 3)))', "from __main__ import count_selected_day; import datetime", number=1)

