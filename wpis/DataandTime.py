from datetime import datetime
from zoneinfo import ZoneInfo

def dowland_now_date():
    zone = ZoneInfo("Europe/Warsaw")
    date = datetime.now(tz=zone)
    return date
if __name__ == '__main__':
    print(dowland_now_date())