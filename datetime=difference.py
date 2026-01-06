from datetime import datetime




day1 = input('enter first dat/time (MM/DD/YY HH:MM) : ')
day2 = input('Enter second dat/time (MM/DD/YY HH:MM) : ')




fmt = '%m/%d/%y %H:%M'
t1 = datetime.strptime(day1, fmt)
t2 = datetime.strptime(day2, fmt)


seconds = (t2 - t1).total_seconds()
print('Seconds Between: ', seconds)


minutes = (seconds/60)
print('Minutes Between: ', minutes)


hours = (minutes/60)
print('Hours Between: ', hours)

days = (hours/24)
print('Days Between: ', days)

years = (days/365)
print('Years Between: ', years)




print('The total time between dates is: ' +
      str(years) + ' Years ' +
      str(days) + ' Days ' +
      str(hours) + ' Hours ' +
      str(minutes) + ' Minutes ' +
      str(seconds) + ' Seconds')





