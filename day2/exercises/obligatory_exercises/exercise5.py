import datetime

def time_until_january_1st():
    current_date = datetime.datetime.now()
    next_year = datetime.datetime(current_date.year + 1, 1, 1)
    time_left = next_year - current_date

    days_left = time_left.days
    hours_left, remainder = divmod(time_left.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)

    print(f"The 1st of January is in {days_left} days and {hours_left}:{minutes_left:02d}:{seconds_left:02d} hours")

time_until_january_1st()
