# Exercise 4: Current Date

import datetime

today_date = datetime.date.today()
actual_datetime = datetime.datetime.now()

print(f"Today's date:", today_date)
print("Current date and time:", actual_datetime)

print(f"Today's date:, {today_date.strftime("%d/%m")}")