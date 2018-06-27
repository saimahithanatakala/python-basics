from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
print (timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print ("today is: " + str(now))


print ("one year from now it will be: " + str(now + timedelta(days=365)))


print ("in two weeks and 3 days it will be: " + str(now + timedelta(weeks=2, days=3)))


t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print ("one week ago it was " + s)
