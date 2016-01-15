import datetime

def add_gigasecond(birthdate):
    gigabirthday = datetime.timedelta(seconds = 10**9)
    return birthdate + gigabirthday
