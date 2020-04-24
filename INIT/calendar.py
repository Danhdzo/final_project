# date stuff
from datetime import date, timedelta

booking_days = []


def months_covered_count(start_date: date, end_date: date):
    return (end_date.year - start_date.year) * 12 + end_date.month - start_date.month + 1


def years_covered_count(start_date: date, end_date: date):
    return ((end_date.year - start_date.year) + 1)


def years_covered(start_day, start_month, start_year, end_day, end_month, end_year):
    months = []
    start = date(int(start_year), int(start_month), int(start_day))
    end = date(int(end_year), int(end_month), int(end_day))

    print('start date: {}'.format(start))
    print('end date: {}'.format(end))
    print('months covered: {}'.format(months_covered_count(start, end)))
    print('years covered: {}'.format(years_covered_count(start, end)))

    months_days = {1: 31,
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
                   12: 31}

    # 1. days in starting month
    # 2. days in ending month
    # 3. days in months in between
    year_count = years_covered_count(start, end)
    total_per_month = []

    for i in range(0, year_count):

        year = start.year + i
        print(year)
        if year_count == 1:
            month_range = range(start.month, end.month + 1)
        elif year == start.year:
            month_range = range(start.month, 13)
        elif year == end.year:
            month_range = range(1, end.month + 1)
        else:
            month_range = range(1, 13)

        for j in month_range:
            # if i is starting month
            if j == start.month and year == start.year:
                day_count = months_days[j] - start.day
            # i is ending month
            elif j == end.month and year == end.year:
                day_count = end.day
            else:
                day_count = months_days[j]
            months.append(j)
            booking_days.append(day_count)
            if j <= 3 or j >= 11:
                rate = 800
            elif j == 4 or j >= 9:
                rate = 1000
            else:
                rate = 1200
            total_per_month.append(rate)

    return (months, booking_days, total_per_month)


start_day = 1
start_month = 1
start_year = 2020
end_day = 1
end_month = 1
end_year = 2021
