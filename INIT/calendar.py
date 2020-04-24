# date stuff
from datetime import date

from INIT.models import Rates, Agents


def days_in_months():
    global booking_days, total
    global day_count
    global month_range
    global month_rate
    def months_covered_count(start_date: date, end_date: date):
        return (end_date.year - start_date.year) * 12 + end_date.month - start_date.month + 1

    def years_covered_count(start_date: date, end_date: date):
        return ((end_date.year - start_date.year) + 1)

    start = date(form.from_year.data, form.from_month, form.from_day)
    end = date(form.to_year.data, form.to_month.data, form.yo_day.data)

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
        booking_days = []
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

            booking_days.append(day_count)

    for r in Rates.query.all():
        for m in month_range:
            if r.month == m:
                rate =r.rate*booking_days[m]
                for a in Agents.query.all():
                    if form.agents.data == a.code:
                        if a.code == 'AMIGUIS':
                            rate=rate*(1-.25)
                            month_rate.append(rate)
                        elif a.code == 'UTE':
                            rate=rate*(1-.3)
                            month_rate.append(rate)
                        elif a.code == 'MILITAR':
                            rate=rate*(1-.1)
                            month_rate.append(rate)

    for val in month_rate:
        total=val[month_rate]+total
    return (booking_days,month_range,month_rate)
    # print(booking_days)
    # print(total_per_month)
    # print(len(total_per_month))
# print('Total: {}'.format(sum(total_per_month)))
