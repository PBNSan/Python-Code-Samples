def hours2days(val):
    days = int(val / 24)
    hours = val % 24
    return days, hours


hours2days(25)