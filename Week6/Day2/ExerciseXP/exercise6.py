#  Exercise 6: Birthday and minutes

import datetime

def minutes_lived(birthdate_str):
    # Parse the birthdate string to a datetime object
    birthdate = datetime.datetime.strptime(birthdate_str, "%d-%m-%Y")
    now = datetime.datetime.now()
    # Calculate the time difference
    time_lived = now - birthdate
    # Get total minutes lived
    total_minutes = int(time_lived.total_seconds() // 60)
    print(f"You have lived for {total_minutes} minutes.")

# Example usage:
minutes_lived("09-07-2005")