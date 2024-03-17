import datetime

def beauty_date() -> str:
    return datetime.date.today().strftime("%A %d %B %Y")