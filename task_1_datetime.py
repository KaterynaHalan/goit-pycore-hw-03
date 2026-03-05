from datetime import datetime

def get_days_from_today(date: str) -> int:
    date_format = "%Y-%m-%d"

    try:
        datetime_obj = datetime.strptime(date, date_format)
    except ValueError:
        return print("Date provided has incorrect format. Please use the format 'yyyy-mm-dd'")

    today = datetime.today()
    return (today - datetime_obj).days
