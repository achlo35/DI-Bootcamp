# Exercise 5: Amount of time left until January 1st

import datetime

todays_date = datetime.date.today()
actual_datetime = datetime.datetime.now()
new_year = datetime.date(todays_date.year + 1, 1, 1)
time_left = new_year - todays_date

print(f"Today's date: {todays_date}")
print(f"Current date and time: {actual_datetime}")
print(f"Time left until January 1st: {time_left.days} days")
print(f"Time left until January 1st: {time_left}")