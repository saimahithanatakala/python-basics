#if loop
password=input("enter the password ")
if password=="MNB":
    print("welcome Mr.Bond")



#if...else
password=input("enter the password ")
if password=="MNB":
    print("welcome Mr.Bond")
else:
    print("access denied")



#if...elif...else
num=float(input("enter the number "))
if num > 4:
          letter='A'
elif num > 3 :
          letter='B'
elif num > 2 :
          letter='C'
else:
          letter ='D'
print("the grade is ",letter)
