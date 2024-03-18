import datetime

def long_date(todays_date: datetime.date) -> str:
    return todays_date.strftime("%A %d %B %Y")