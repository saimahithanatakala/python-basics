#creating html calender
import calendar
hc=calendar.HTMLCalendar(calendar.SUNDAY)
str=hc.formatmonth(2018,5)
print(str)
