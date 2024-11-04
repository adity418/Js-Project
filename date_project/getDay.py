# enter the date and get Day as output

import datetime

date_str = input("Enter the date in format yyyy-mm-dd : ")

date_obj = datetime.datetime.strptime(date_str,'%Y-%m-%d').date()

day = date_obj.strftime('%A')

print(f"The day name for {date_obj} is: {day}")