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


def get_count_day(first_day_index, count_work_days):
    """
    Количество календарных дней начиная с дня недели(first_day) и имея work_days рабочих дней
    @first_day - int(0-6)
    @work_days - int

    @return int
    """
    count_work_days = abs(count_work_days)
    if first_day_index < 0:
        first_day_index = 0
    if first_day_index > 6:
        first_day_index = 6
    full_week_count = count_work_days / 5 + 1
    if count_work_days + first_day_index > 5 and full_week_count == 1:
        full_week_count = 2
    weekday_range = (range(7) * full_week_count)[first_day_index:]
    weekends_count = (7 - 5) * (full_week_count - 1)
    if first_day_index > 4:
        weekends_count -= 7 - first_day_index
    last_day_index = len(weekday_range[first_day_index:]) - count_work_days - weekends_count
    return len(weekday_range[first_day_index:-last_day_index])


def get_last_day(start_date, count_work_days):
    """
    Дату последнего дня после count_work_days будних дней
    """
    return start_date + datetime.timedelta(days=get_count_day(start_date.weekday(), count_work_days))


def work_day_count(start_date, work_days, need_days={0, 1, 2, 3, 4}):
    n = 0
    while n < work_days:
        if start_date.weekday() in need_days:
            n += 1
        start_date += datetime.timedelta(days=1)
    return start_date


def _deadline_start(date, days):
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
#print _deadline_start('2013-08-01', 3)
#print timeit.timeit('_deadline_start("2013-08-01", 10000)', "from __main__ import _deadline_start; import datetime; import pytz", number=1)
#print get_last_day(datetime.date(2013, 8, 1), 3)
#print timeit.timeit('datetime.date(2013, 8, 1) + datetime.timedelta(days=len(count_selected_day(datetime.date(2013, 8, 1), 10000)))', "from __main__ import count_selected_day; import datetime", number=1)
#print get_last_day(datetime.date(2013, 8, 1), 3)
#print timeit.timeit('datetime.date(2013, 8, 1) + datetime.timedelta(days=len(count_selected_day(datetime.date(2013, 8, 1), 10)))', "from __main__ import count_selected_day; import datetime", number=1)
#print timeit.timeit('datetime.date(2013, 8, 1) + datetime.timedelta(days=len(count_selected_day(datetime.date(2013, 8, 1), 3)))', "from __main__ import count_selected_day; import datetime", number=1)

