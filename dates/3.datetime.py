from datetime import datetime
now=datetime.now()
print (now.strftime("The current year is: %Y")) 
print (now.strftime("%a, %d %B, %y"))
print(now.strftime("%A,%D %b,%Y"))
