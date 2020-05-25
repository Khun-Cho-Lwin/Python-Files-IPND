def show_day(enter_day):
    month_day = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
    result_day = (enter_day + 0) % 7
    return month_day[result_day]
print show_day(31)
print show_day(9)
