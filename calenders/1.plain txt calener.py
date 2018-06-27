#creating a plain txt calender
import calendar
c=calendar.TextCalendar(calendar.MONDAY)
str=c.formatmonth(2018,5)
print(str)
