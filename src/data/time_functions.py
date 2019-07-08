def get_last_day(month):
    if month==2: #sleep year check
        return 28
    else:
        if month in (4,6,9,11):
            return 30
        else:
            return 31

def get_previous_year(year, month):
    if month == 1:
        return year-1
    else:
        return year

def get_previous_month(month):
    if month == 1:
        return 12
    else:
        return month -1

def get_next_year(year, month):
    if month == 12:
        return year+1
    else:
        return year

def get_next_month(month):
    if month == 12:
        return 1
    else:
        return month +1
