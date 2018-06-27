import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
for i in c.itermonthdays(2018, 2):             #all dates
  print (i)

for name in calendar.month_name:               #printing monthes
    print(name)


for day in calendar.day_name:                  #priting days
    print(day)
