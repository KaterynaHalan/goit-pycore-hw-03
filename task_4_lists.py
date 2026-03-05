from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    date_format = "%Y.%m.%d"
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], date_format).date()

        # Replace birthday in the current year
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            # Move weekend days to Monday
            weekday = congratulation_date.weekday()
            if weekday == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif weekday == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime(date_format)
            })

    return result
